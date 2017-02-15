import pickle
from split_text import spliter
from get_recalls import random_recalls
import random

def emotions(string, machine, vectorizer):
    return machine.predict(vectorizer.transform([spliter(string)]))[0]

def rand_recall():
    with open('Teached.pkl', 'rb') as line:
        linear = pickle.load(line)
    line.close()
    with open('Vectoriser.pkl', 'rb') as vec:
        vector = pickle.load(vec)
    vec.close()
    with open('not_rated.pkl', 'rb') as vec:
        not_rated = pickle.load(vec)
    vec.close()


    num_range = int(len(not_rated))
    num = random.randint(0, num_range-1)
    recalls =not_rated
    link = ""
    answer =recalls[num]
    emotion = emotions(recalls[num], linear, vector)
    return answer, link, emotion