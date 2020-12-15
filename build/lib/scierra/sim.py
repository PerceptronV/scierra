from scierra.compile import build, run
from scierra.utils import gen_name, working_dir, count, replace_string, replace_comment, count_fors, empty_couts
import os

OUT_SUPPORT = [
    'using',
    '#include',
    'typedef',
    '#define',
    'void',
    'return',
    'class'
]


class Simulator(object):
    def __init__(self):
        self.wdir = working_dir()
        self.bef_mains = ""
        self.mains = ""
        self.buff = ""
        self.TEMPLATE = "#include<iostream>\n#include<sstream>\n#include<fstream>\n#include<vector>\n#include<string>\nusing namespace std;\n{}\n{}\n"

    def addline(self, line):
        self.buff += line
        proc, str_dict = replace_string(self.buff)
        proc, com_dict = replace_comment(proc)

        if (count(proc, '{') <= count(proc, '}')) and \
                (count(proc, ';') >= (count_fors(proc) * 2 + 1) or '#' in proc):
            out = False
            for i in OUT_SUPPORT:
                if count(proc, i, syntax=True) > 0:
                    out = True

            if out:
                if self.invoke(empty_couts(self.bef_mains) + self.buff, empty_couts(self.mains)):
                    self.bef_mains += self.buff

            else:
                if self.invoke(empty_couts(self.bef_mains), empty_couts(self.mains) + self.buff):
                    self.mains += self.buff

            self.buff = ""
            return True

        else:
            return False

    def invoke(self, bef_mains, mains, src_name = None, exe_name = None):
        code = "#include<iostream>\nusing namespace std;\n{}\n{}\n".format(
            bef_mains, 'int main(){\n' + mains + '\nreturn 0;}'
        )

        if src_name == None:
            src_name = gen_name(self.wdir, '.cpp')
        if exe_name == None:
            exe_name = gen_name(self.wdir, '.exe')
        cin_name = gen_name(self.wdir, '.cin')

        f = open(src_name, 'w')
        f.write(code)
        f.close()

        ret = build(self.wdir, src_name, exe_name)
        if ret:
            ret = run(self.wdir, exe_name) == 0
            os.remove(os.path.join(self.wdir, exe_name))

        os.remove(os.path.join(self.wdir, src_name))

        return ret

    def print_code(self):
        code = self.TEMPLATE.format(
            self.bef_mains, 'int main(){\n' + self.mains + '\nreturn 0;}'
        )
        print(code)

    def restart(self):
        self.wdir = working_dir()
        self.bef_mains = ""
        self.mains = ""
        self.buff = ""
