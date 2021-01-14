from scierra.compile import build, run
from scierra.utils import gen_name, working_dir, count, replace_string, replace_comment, empty_couts, isblock
import os
import platform

KEYWORDS = {
    'exp_prep':[
        '#*include',
        '#*define'
    ],
    'prep': [
        'typedef',
        'using'
    ],
    'glob': [
        'class',
        'struct',
        'return',
        'void',
        'template',
        'typename'
    ]
}

FILE_EXTENSION = {
    'Windows': '.exe',
    'Linux': '.out',
    'Darwin': '.out'
}


class Simulator(object):
    def __init__(self):
        self.wdir = working_dir()
        self.preprocs = ""
        self.globals = ""
        self.mains = ""
        self.buff = ""
        self.TEMPLATE = "#include<iostream>\n#include<sstream>\n#include<fstream>\n#include<vector>\n#include<string>\nusing namespace std;\n{}\n{}\n{}\n"

    def gen_code(self, preps=None, globs=None, mains=None):
        if preps is None:
            preps = self.preprocs
        if globs is None:
            globs = self.globals
        if mains is None:
            mains = self.mains

        code = self.TEMPLATE.format(
            preps, globs, 'int main(){\n' + mains + '\nreturn 0;\n}'
        )

        return code

    def addline(self, line):
        self.buff += line
        proc, str_dict = replace_string(self.buff)
        proc, com_dict = replace_comment(proc)

        if isblock(proc):
            section = 'main'

            if '<prep>' in proc:
                section = 'prep'
                proc = proc.replace('<prep>', '')
            elif '<glob>' in proc:
                section = 'glob'
                proc = proc.replace('<glob>', '')
            elif '<main>' in proc:
                section = 'main'
                proc = proc.replace('<main>', '')
            else:
                for i in KEYWORDS['glob']:
                    if count(proc, i, syntax=True) > 0:
                        section = 'glob'

                for i in KEYWORDS['prep']:
                    if count(proc, i, syntax=True) > 0:
                        section = 'prep'

                for i in KEYWORDS['exp_prep']:
                    if count(proc, i, exp=True) > 0:
                        section = 'prep'

            for i in com_dict:
                proc = proc.replace(i, com_dict[i])
            for i in str_dict:
                proc = proc.replace(i, str_dict[i])
            self.buff = proc

            if section == 'prep':
                if self.invoke(self.preprocs + self.buff, self.globals, empty_couts(self.mains)):
                    self.preprocs += self.buff
            elif section == 'glob':
                if self.invoke(self.preprocs, self.globals + self.buff, empty_couts(self.mains)):
                    self.globals += self.buff
            elif section == 'main':
                if self.invoke(self.preprocs, self.globals, empty_couts(self.mains) + self.buff):
                    self.mains += self.buff

            self.buff = ""
            return True

        elif proc[0] == '<' and proc[:6] not in ['<prep>', '<glob>', '<main>']:
            self.buff = 'cout << ' + self.buff[1:] + ';'
            self.invoke(self.preprocs, self.globals, empty_couts(self.mains) + self.buff)
            self.buff = ""
            return True

        else:
            return False

    def invoke(self, preps, globs, mains, src_name=None, out_name=None):
        code = self.gen_code(preps, globs, mains)

        if src_name is None:
            src_name = gen_name(self.wdir, 'scierra-', '.cpp')
        if out_name is None:
            out_name = gen_name(self.wdir, 'scierra-', FILE_EXTENSION[platform.system()])

        f = open(src_name, 'w')
        f.write(code)
        f.close()

        ret = build(self.wdir, src_name, out_name)
        if ret:
            ret = run(self.wdir, out_name)==0
            os.remove(os.path.join(self.wdir, out_name))

        os.remove(os.path.join(self.wdir, src_name))

        return ret

    def print_code(self):
        print(self.gen_code())

    def restart(self):
        self.__init__()
