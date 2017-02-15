import pymorphy2

dnoun = {"nomn": 0, "gent": 1, "datv": 2, "accs": 3, "ablt": 4, "loct": 5, "loc2": 5, "gen2": 1, "acc2": 3,
         "voct": 6}
dnum = {"femn": 1, "plur": 0, "masc": 2, "neut": 3}

morph = pymorphy2.MorphAnalyzer()

def work(g):
    qw = 1000000007
    p = 2003
    ans = set()
    ss = []
    a = ''
    f = 0
    for j in g:
        if j == ' ' or j == '\n':
            ss.append(a)
            f = 0
            a = ''
            continue
        if j in ',./!?-"():;$%“”':
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
    if a != '':
        ss.append(a)
    noun = [[[] for ii in range(7)] for jj in range(4)]
    verb = []
    verin = []
    adv = []
    adj = [[[] for ii in range(7)] for jj in range(4)]
    s = set()
    for i in ss:
        if len(i) == 0 or i[0] in ',./!?-"():;$%“”' or ord(i[0]) < 1000:
            for l in range(7):
                for k in range(4):
                    for x in noun[k][l]:
                        for y in adj[k][l]:
                            s.add((y, x))
            for x in verb:
                for y in noun[0][0]:
                    s.add((y, x))
                for y in noun[1][0]:
                    s.add((y, x))
                for y in adv:
                    s.add((y, x))
                for y in verin:
                    s.add((x, y))
            for x in s:
                ans.add(x)
            s = set()
            noun = [[[] for ii in range(7)] for jj in range(4)]
            verb = []
            adv = []
            adj = [[[] for ii in range(7)] for jj in range(4)]
            continue
        q = morph.parse(i)
        for j in q:
            if "Abbr" in j.tag or j.tag.POS is None:
                continue
            s = set()
            h = j.normal_form
            has = 0
            for l in h:
                has = (has * p + ord(l)) % qw
            has = h
            if ' ' in has:
                print(has, i, "      ", g)
                s = []
            ans.add((has, has))
            if j.tag.POS in "NOUN NUMR PRED NPRO":
                if j.tag.case is not None:
                    if j.tag.number is not None:
                        if j.tag.number == "plur":
                            noun[dnum[j.tag.number]][dnoun[j.tag.case]].append(has)
                        elif j.tag.gender is not None:
                            noun[dnum[j.tag.gender]][dnoun[j.tag.case]].append(has)
                        else:
                            for l in range(1, 4):
                                noun[l][dnoun[j.tag.case]].append(has)
                    else:
                        for l in range(4):
                            noun[l][dnoun[j.tag.case]].append(has)
                else:
                    for l in range(7):
                        if j.tag.number is not None:
                            if j.tag.number == "plur":
                                noun[dnum[j.tag.number]][l].append(has)
                            elif j.tag.gender is not None:
                                noun[dnum[j.tag.gender]][l].append(has)
                            else:
                                for ll in range(1, 4):
                                    noun[ll][l].append(has)
                        else:
                            for ll in range(2):
                                noun[ll][l].append(has)
            elif j.tag.POS in "ADJF ADJS COMP PRTF PRTS":
                if j.tag.case is not None:
                    if j.tag.number is not None:
                        if j.tag.number == "plur":
                            adj[dnum[j.tag.number]][dnoun[j.tag.case]].append(has)
                        elif j.tag.gender is not None:
                            adj[dnum[j.tag.gender]][dnoun[j.tag.case]].append(has)
                        else:
                            for l in range(1, 4):
                                adj[l][dnoun[j.tag.case]].append(has)
                    else:
                        for l in range(4):
                            adj[l][dnoun[j.tag.case]].append(has)
                else:
                    for l in range(7):
                        if j.tag.number is not None:
                            if j.tag.number == "plur":
                                adj[dnum[j.tag.number]][l].append(has)
                            elif j.tag.gender is not None:
                                adj[dnum[j.tag.gender]][l].append(has)
                            else:
                                for ll in range(1, 4):
                                    adj[ll][l].append(has)
                        else:
                            for ll in range(2):
                                adj[ll][l].append(has)
            elif j.tag.POS in "VERB INFN":
                verb.append(has)
            elif j.tag.POS in "GRND ADVB":
                adv.append(has)
            if j.tag.POS == "INFN":
                verin.append(has)
    #print(ans)
    return ans

fgood = open("good.txt", "r")
fbad = open("bad.txt", "r")
s = fgood.readlines()
d = dict()
for i in s:
    j = i.split()
    if int(j[-1]) > 1 and len(j) >= 3:
        d[(j[0], j[1])] = [int(j[-1]) * 1.4 / 3893, 0] #153
s = fbad.readlines()
for i in s:
    j = i.split()
    if int(j[-1]) > 3 and len(j) >= 3:
        if (j[0], j[1]) in d:
            d[(j[0], j[1])][1] = int(j[-1]) / 13031
        else:
            d[(j[0], j[1])] = [0, int(j[-1]) / 13031]

def emotion(text):
    h = text + '.'
    ans = work(h)
    c = 0
    for i in ans:
        if i in d:
            # print(d[i][0], d[i][1])
            c += (d[i][0] - d[i][1]) / (d[i][0] + d[i][1])
    if c >= 0:
        m = "Положительно"
    else:
        m = "Отрицательно"
    return m