from flask import Flask, render_template, request
import pickle
from Emotions_final import rand_recall, emotions
from program import  emotion
from project import  predict
from function import function
app = Flask(__name__)

with open('Teached.pkl', 'rb') as line:
    linear = pickle.load(line)
line.close()
with open('Vectoriser.pkl', 'rb') as vec:
    vector = pickle.load(vec)
vec.close()

@app.route("/first_model", methods=["POST", "GET"])
def index_page(default="""В тот момент, когда Вы нажимаете кнопку, программа выбирает случаный банк с сайта banki.ru, после чего показывает все отзывы от пользоватлей о найденном учреждении, затем оценивает их эмоциональную окраску и выводит к нам на сайт.""", users="Введите ваш отзыв", rate = "0"):
    try:
        if request.method == "POST" and request.form["generate"] == u"Сгенерировать":
            recall = rand_recall()
            default = recall[0]
            if recall[2] > 0:
                rate = u"Положительный"
            else:
                rate = u"Отрицательный"
            rate += " (" + str(recall[2]) + ")"
    except:
        pass
    try:
        if request.method == "POST" and request.form["rating"] == u"Оценить":
            text = request.form["text"]
            users = text
            rate = u"Положительный" + " (" + str(emotions(text, linear, vector)) + ")" if emotions(text, linear, vector) > 0 else u"Отрицательный" + " (" + str(emotions(text, linear, vector)) + ")"

    except:
        pass
    return render_template('first_model.html', random_comment=default, user_recall=users, rate=rate)

@app.route("/second_model", methods=["POST", "GET"])
def modelling_2(default="""В тот момент, когда Вы нажимаете кнопку, программа выбирает случаный банк с сайта banki.ru, после чего показывает все отзывы от пользоватлей о найденном учреждении, затем оценивает их эмоциональную окраску и выводит к нам на сайт.""", users="Введите ваш отзыв", rate = "0"):
    try:
        if request.method == "POST" and request.form["generate2"] == u"Сгенерировать":
            recall = rand_recall()
            default = recall[0]
            rate = emotion(default)
    except:
        pass
    try:
        if request.method == "POST" and request.form["rating2"] == u"Оценить":
            text = request.form["text"]
            users = text
            rate = emotion(text)

    except:
        pass
    return render_template('second_model.html', random_comment=default, user_recall=users, rate=rate)

@app.route("/third_model", methods=["POST", "GET"])
def modelling_3(default="""В тот момент, когда Вы нажимаете кнопку, программа выбирает случаный банк с сайта banki.ru, после чего показывает все отзывы от пользоватлей о найденном учреждении, затем оценивает их эмоциональную окраску и выводит к нам на сайт.""", users="Введите ваш отзыв", rate = "Ничего"):
    try:
        if request.method == "POST" and request.form["generate3"] == u"Сгенерировать":
            recall = rand_recall()
            default = recall[0]
            rate = predict(default)
    except:
        pass
    try:
        if request.method == "POST" and request.form["rating3"] == u"Оценить":
            text = request.form["text"]
            users = text
            rate = predict(text)

    except:
        pass
    return render_template('third_model.html', random_comment=default, user_recall=users, rate=rate)

@app.route("/fourth_model", methods=["POST", "GET"])
def modelling_4(default="""В тот момент, когда Вы нажимаете кнопку, программа выбирает случаный банк с сайта banki.ru, после чего показывает все отзывы от пользоватлей о найденном учреждении, затем оценивает их эмоциональную окраску и выводит к нам на сайт.""", users="Введите ваш отзыв", rate = "Ничего"):
    try:
        if request.method == "POST" and request.form["generate4"] == u"Сгенерировать":
            recall = rand_recall()
            default = recall[0]
            rate = function(default)
    except:
        pass
    try:
        if request.method == "POST" and request.form["rating4"] == u"Оценить":
            text = request.form["text"]
            users = text
            rate = function(text)

    except:
        pass
    return render_template('fourth_model.html', random_comment=default, user_recall=users, rate=rate)
@app.route("/", methods=["POST", "GET"])
def starting():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
