import re

def diophantine_parser(input):
    s = input.strip()
    dic = {}

    if re.match('-?\d{0,4}[xy][\-,\+]\d{0,4}[xy]=-?\d{0,4}', s):
        fst_spl = s.split('=')
        dic.update({"n": int(fst_spl[1])})
        snd_spl = re.findall('[\-,\+]?\d{0,4}[xy]', s)

        if ('x' in snd_spl[0] and 'y' in snd_spl[1]):
            index_x = 0
            index_y = 1
        elif('x' in snd_spl[1] and 'y' in snd_spl[0]):
            index_x = 1
            index_y = 0
        else:
            raise ValueError('Invalid_input')

        coef_x = snd_spl[index_x].strip('+x')

        if coef_x == '':
            dic.update({"x": 1})
        elif coef_x == '-':
            dic.update({"x": -1})
        else:
            dic.update({"x": int(coef_x)})

        coef_y = snd_spl[index_y].strip('+y')

        if coef_y == '':
            dic.update({"y": 1})
        elif coef_y == '-':
            dic.update({"y": -1})
        else:
            dic.update({"y": int(coef_y)})

        return dic

    else:
        raise ValueError('Invalid_input')
