from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, world!"


@app.route('/about/')
def about():
    return "about"


@app.route('/contact/')
def contact():
    return "contact"


@app.route('/<int:num1>/<int:num2>')
def summa(num1, num2):
    return f"{num1 + num2}"


@app.route('/string/<line>')
def get_len(line):
    return f"{len(line)}"


html_temp = """
    <h1>Моя первая HTML-страница</h1>
    <p>Привет, мир!</p>
"""


@app.route('/html')
def html():
    return html_temp


_students = [
    {"name": "Иван", "sname": "Иванов", "age": 20, "avg_score": 5},
    {"name": "Иван", "sname": "Петров", "age": 20, "avg_score": 5},
    {"name": "Иван", "sname": "Сидоров", "age": 20, "avg_score": 5},
]


@app.route('/table')
def table():
    return render_template("students.html", students=_students)


_news = [
    {"title": "Новость1", "description": "Описание новости 1", "date": "20.02.2023"},
    {"title": "Новость2", "description": "Описание новости 2", "date": "20.02.2023"},
    {"title": "Новость3", "description": "Описание новости 3", "date": "20.02.2023"}
]


@app.route('/news/')
def news():
    return render_template("news.html", news=_news)


if __name__ == "__main__":
    app.run(debug=True)
