from flask import Flask, g, redirect, request, render_template, send_from_directory
from os import path, urandom

from .auth import bp, login_required
from .model import db, Items, User


app = Flask(__name__)

if not path.exists("secret_key.txt"):
    flask_secret_key = urandom(24)
    with open("secret_key.txt", "a") as file:
        file.write(flask_secret_key)

with open("secret_key.txt", "r") as file:
    app.secret_key = file.read()

app.config.from_object("riolists.config.Config")
db.init_app(app)
app.register_blueprint(bp)


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/", methods=["GET", "POST"])
@login_required
def main_page():
    if request.method == "GET":
        user = User.query.get(g.user.id)
        items = Items.query.with_parent(user).filter(Items.is_active).order_by(
            Items.date_created.desc()
        ).all()
        return render_template("main.html", items=items)
    if request.method == "POST":
        action = request.form["action"]
        if action == "item_add":
            text = request.form["text"]
            amount = request.form["amount"]
            item = Items(text=text, amount=amount, user_id=g.user.id)
            db.session.add(item)
        if action == "item_deactivate":
            item_id = request.form["item_id"]
            user_id = g.user.id
            item = Items.query.filter_by(id=item_id, user_id=user_id).first()
            if item is not None:
                item.is_active = False
        db.session.commit()
        return redirect(request.url)


@app.route("/about")
def about_page():
    return render_template("about.html")
