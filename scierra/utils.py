import os, random


class utils():
    def rndstr(l):
        s = ''
        for i in range(l):
            s += chr(random.randint(97, 122))
        return s


    def gen_name(dir, ext, l=8):
        s = rndstr(l) + ext
        while os.path.exists(os.path.join(dir, s)):
            s = rndstr(l) + ext
        return s


    def working_dir():
        return os.getcwd()


    def count(str, k, syntax=False):
        r = 0
        l = len(k)

        if str[:l] == k:
            if syntax:
                if not str[l].isalnum():
                    r += 1
            else:
                r += 1

        for i in range(1, len(str)):
            if str[i:i+l] == k:
                if syntax:
                    if not str[i - 1].isalnum() and not str[i + l].isalnum():
                        r += 1
                else:
                    r += 1

        return r


    def skip_whitespaces(str, index):
        WHITESPACES = [' ', '\r', '\t', '\n']

        i = index + 1
        while str[i] in WHITESPACES:
            i += 1
            if i == len(str):
                return None

        return str[i]


    def count_fors(str):
        r = 0
        for i in range(len(str) - 3):
            if (str[i:i+3] == 'for') and (not str[i-1].isalnum()) and (skip_whitespaces(str, i+2) == '('):
                r += 1

        return r


    def empty_couts(str):
        proc, dictionary = replace_string(str)
        ret = ''
        in_cout = False

        for i in range(len(proc)):
            if not in_cout and i < len(proc)-4:
                if (proc[i:i+4] == 'cout') and (not proc[i-1].isalnum()) and (skip_whitespaces(proc, i+3) == '<'):
                    in_cout = True
                    ret += 'cout << "";'
                else:
                    ret += proc[i]

            elif in_cout and proc[i] == ';':
                in_cout = False

            elif not in_cout:
                ret += proc[i]

        for i in dictionary:
            ret = ret.replace(i, dictionary[i])

        return ret


    def replace_string(s, str_tok_pre='~STR', str_tok_suf='~'):
        ret = ''
        count = 0
        dictionary = {}
        tok = None

        in_string = False
        in_char = False

        for i in range(len(s)):
            if s[i] == '"' and s[i - 1] != '\\' and not in_char:
                in_string = not in_string
                if in_string:
                    tok = str_tok_pre + str(count) + str_tok_suf
                    ret += tok
                    dictionary[tok] = '"'
                    count += 1
                else:
                    dictionary[tok] += '"'

            elif s[i] == "'" and s[i - 1] != '\\' and not in_string:
                in_char = not in_char
                if in_char:
                    tok = str_tok_pre + str(count) + str_tok_suf
                    ret += tok
                    dictionary[tok] = "'"
                    count += 1
                else:
                    dictionary[tok] += "'"

            elif not in_char and not in_string:
                ret += s[i]

            else:
                dictionary[tok] += s[i]

        return ret, dictionary


    def replace_comment(s, com_tok_pre='~COM', com_tok_suf='~'):
        ret = ''
        count = 0
        dictionary = {}
        tok = None

        in_single = False
        in_multi = False

        for i in range(len(s)):
            if (s[i] == '/' and s[i - 1] == '/') and (not in_single and not in_multi):
                in_single = True
                tok = com_tok_pre + str(count) + com_tok_suf
                ret = ret[:-1] + tok
                dictionary[tok] = '//'
                count += 1

            elif (s[i] == '\n' and s[i - 1] != '\\') and in_single:
                in_single = False
                ret += '\n'
                dictionary[tok] += '\n'

            elif (s[i] == '*' and s[i - 1] == '/') and (not in_single and not in_multi):
                in_multi = True
                tok = com_tok_pre + str(count) + com_tok_suf
                ret = ret[:-1] + tok
                dictionary[tok] = '/*'
                count += 1

            elif (s[i] == '/' and s[i - 1] == '*') and in_multi:
                in_multi = False
                dictionary[tok] += '/'

            elif not in_single and not in_multi:
                ret += s[i]

            else:
                dictionary[tok] += s[i]

        return ret, dictionary
