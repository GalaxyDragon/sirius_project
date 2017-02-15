from sklearn import cross_validation
import numpy as np
import pickle
from Emotions_final import  emotions
from program import  emotion
from project import  predict
from function import function
with open('Teached.pkl', 'rb') as line:
    linear = pickle.load(line)
line.close()
with open('Vectoriser.pkl', 'rb') as vec:
    vector = pickle.load(vec)
vec.close()

def line(s):
    return emotions(s, linear, vector)


def testing(text, rates, function_now):
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    for i in range(592):
        pred = function_now(text[test_nums[i]])
        prediction = pred
        real = rates[test_nums[i]]
        if(pred == "Положительно"):
            prediction = 1
        elif(pred == "Отрицательно"):
            prediction = -1
        pred=prediction
        if (pred>0):
            prediction = 1
        else:
            prediction = -1
        if prediction == -1 and real == -1:
            true_negative += 1
        if prediction == -1 and real == 1:
            false_negative += 1
        if prediction == 1 and real == -1:
            false_positive += 1
        if prediction == 1 and real == 1:
            true_positive += 1
    precision_for_positive = true_positive / (true_positive + false_positive)
    recall_for_positive = true_positive / (true_positive + false_negative)
    precision_for_negative = true_negative / (true_negative + false_negative)
    recall_for_negative = true_negative / (true_negative + false_positive)
    accuraty = (true_negative + true_positive) / (true_negative + true_positive + false_negative + false_positive)
    F1_for_positive = 2 * (precision_for_positive * recall_for_positive) / (precision_for_positive + recall_for_positive)
    F1_for_negative = 2 * (precision_for_negative * recall_for_negative) / (precision_for_negative + recall_for_negative)
    return accuraty, F1_for_positive, F1_for_negative




input_good = open('good1.txt')
good = input_good.read().split('],')[1:]
input_good.close()
input_bad = open('bad1.txt')
bad = input_bad.read().split('880035')
for i in range(len(good)):
    good[i] = good[i][2:]
for i in range(1, len(bad)):
    bad[i] = bad[i][1:]
bad = bad[:len(good)]
all_rates = np.array([1] * len(good) + [-1] * len(good))
texts = []
texts.extend(good)
texts.extend(bad)
teach_nums = []
test_nums = []
for teach_nums, test_nums in cross_validation.StratifiedShuffleSplit(all_rates, n_iter=1, test_size=0.1):
    pass

print(testing(texts,all_rates,line))
print(testing(texts, all_rates, predict))
print(testing(texts, all_rates, function))
print(testing(texts, all_rates, emotion))