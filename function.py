import pickle
import pymorphy2 as pm


def function(s4):
    s = s4.split()
    morph = pm.MorphAnalyzer()
    with open('vect.pkl', 'rb') as f:
        vect_new = pickle.load(f)
    with open('model_rfc.pkl', 'rb') as f1:
        for_new = pickle.load(f1)
    s3 = ''
    for j in range(len(s)):
        s1 = ''
        for k in range(len(s[j])):
            if ord('а') <= ord(s[j][k]) <= ord('я') or ord('А') <= ord(s[j][k]) <= ord('Я'):
                s1 = s1 + s[j][k]
        s3 = s3 + ' ' + morph.normal_forms(s1)[0]
    vect = vect_new.transform([s3])
    ans = for_new.predict(vect)[0]
    if ans == 0:
        return 'Отрицательно'
    else:
        return 'Положительно'