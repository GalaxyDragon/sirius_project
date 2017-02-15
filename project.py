import pymorphy2
import pickle


def predict(s):
    morph = pymorphy2.MorphAnalyzer()
    f = open("mod1.pkl", "rb")  # загрузка модели
    model = pickle.load(f)
    vectorizer = pickle.load(f)
    f.close()
    if s[0] == "﻿":  # удаление странного символа
        s = s[1:]
    x = s
    x3 = ""
    x = list(map(str, x.split()))
    for i in range(len(x)):  # нормализация отзыва
        if (x[i][-1] in ",.!)(-+][;:?\/'"):
            x[i] = x[i][:len(x[i]) - 1]
        if (len(x[i]) != 0 and x[i][0] in ",.!)(-+][;:?\/'"):
            x[i] = x[i][1:]
        p = morph.parse(x[i])[0]
        if (x[i] in ",.!)(-+][;:?\/'"):
            continue
        x3 += (p.normal_form) + " "
    if x3[0] == "﻿":  # удаление странного символа 2
        x3 = x3[1:]
    rrr = model.predict_proba(vectorizer.transform([x3]))[0]
    if (model.predict(vectorizer.transform([x3]))[0] == 0):
        return "Положительно" + " " + str((round(rrr[0] * 10000))/100) + "%"
    else:
        return "Отрицательно" + " " + str((round(rrr[1] * 10000))/100) + "%"