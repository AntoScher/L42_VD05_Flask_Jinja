from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def films():
    context = {
        "caption": "Фильмы ",
        "link": "Перейти на страницу героев фильма?",
    }
    return render_template("index.html", **context)
@app.route("/person/")
def person():
    return render_template("main.html", caption="Герои фильмов", link="Вернуться на главную страницу ")

if __name__ == "__main__":
    app.run()