from  flask import Flask, render_template, request, redirect, url_for
from forms import app

posts = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        post = {"title": title, "content": content}
        # создаёт условие для проверки наличия данных в полях title и content
        if title and content:
            posts.append({'title': title, 'content': content})
        # использует для обновления страницы и предотвращения повторной отправки формы.
        # возвращает отрендеренный шаблон с переданными данными постов
        return redirect(url_for("index"))
    return render_template("blog.html", posts=posts)


