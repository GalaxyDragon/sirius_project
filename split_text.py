import pymorphy2


def spliter(review):
    ss = []
    g = review + ' opw'
    a = ''
    f = 0
    for j in g:
        if j == ' ' or j == '\n':
            ss.append(a)
            f = 0
            a = ''
            continue
        if j in ',./!?-"():;$%':
            if not f:
                ss.append(a)
                a = ''
            a += j
            f = 1
            continue
        if f:
            f = 0
            ss.append(a)
            a = ''
        a += j
    ssss = []
    for num in range(len(ss)):
        if ss[num] not in '1234567890%:':
            ssss.append(ss[num])
    if a != '':
        ss.append(a)
    morph = pymorphy2.MorphAnalyzer()
    for j in range(len(ss)):
        q = morph.parse(ss[j])[0]
        ss[j] = q.normal_form
    s = ' '.join(ssss).split()
    sss = []
    for k in range(len(s)):
        q = morph.parse(s[k])[0]
        if 'PREP' != q.tag.POS:
            sss.append(s[k])
    normal_form = ' '.join(sss)
    return normal_form
