from flask import Flask, redirect, request, render_template
from .model import db, Items, User


app = Flask(__name__)
app.config.from_object("riolists.config.Config")
db.init_app(app)


@app.route("/", methods=["GET", "POST", "PUT"])
def main_page():
    if request.method == "GET":
        user = User.query.get(1)
        items = Items.query.with_parent(user).filter(Items.is_active).order_by(
            Items.date_created.desc()
        ).all()
        return render_template("main.html", items=items)
    if request.method == "POST":
        action = request.form["action"]
        if action == "item_add":
            text = request.form["text"]
            amount = request.form["amount"]
            item = Items(text=text, amount=amount)
            db.session.add(item)
        if action == "item_deactivate":
            item_id = request.form["item_id"]
            user_id = request.form["user_id"]
            item = Items.query.filter_by(id=item_id, user_id=user_id).first()
            item.is_active = False
        db.session.commit()
        return redirect(request.url)
