from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def films():
    context = {
        "caption": "Фильмы ",
        "link": "Перейти куда-нибудь"
    }
    return render_template("index.html", **context)


@app.route("/person/")
def person():
    return render_template("main.html", caption="Герои фильмов", link="Перейти? ")


if __name__ == "__main__":
    app.run()