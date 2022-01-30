from flask import Flask, redirect, request, render_template

from db import db, Items, User


app = Flask(__name__)
app.config.from_object("riolists.config.Config")


@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "GET":
        user = User.query.get(1)
        items = Items.query.with_parent(user).filter(Items.is_active).order_by(
            Items.date_created.desc()
        ).all()
        return render_template("main.html", items=items)
    if request.method == "POST":
        text = request.form["text"]
        amount = request.form["amount"]
        item = Items(text=text, amount=amount)
        db.session.add(item)
        db.session.commit()
        return redirect(request.url)
