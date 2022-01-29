from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("riolists.config.Config")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=False, nullable=False)
    name = db.Column(db.String(128), unique=False, nullable=False)

    def __init__(self, login, password, name="TestUser"):
        self.login = login
        self.password = password
        self.name = name

    def __repr__(self):
        return f"{self.id} => {self.login}"


@app.route("/")
def main_page():
    return jsonify(message="sup, dude!")

