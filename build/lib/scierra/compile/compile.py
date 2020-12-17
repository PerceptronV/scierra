import os


def build(filedir, filename, outname):
    cmd = ['cd {}'.format(filedir),
           'g++ -o {} {}'.format(outname, filename)]
    cmd = ' & '.join(cmd)

    a = os.system(cmd)

    if a != 0:
        print('Compilation terminated with return code {}'.format(a))
        return False
    else:
        return True


def run(filedir, filename):
    cmd = ['cd {}'.format(filedir),
           '{}'.format(filename)]
    cmd = ' & '.join(cmd)

    return os.system(cmd)
