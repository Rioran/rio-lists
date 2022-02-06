from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=False, nullable=False)
    name = db.Column(db.String(128), unique=False, nullable=False)
    items = db.relationship("Items")

    def __init__(self, login, password, name=None):
        self.login = login
        self.password = password
        if name is None:
            name = login
        self.name = name
        print(f"User {self.name} added")

    def __repr__(self):
        return f"{self.id} => {self.login}"


class Items(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date_created = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    text = db.Column(db.String(100), nullable=True)
    amount = db.Column(db.Float, nullable=True)

    def __init__(self, user_id=1, text="-no-text-", amount=0):
        self.user_id = user_id
        self.text = text
        self.amount = amount
        self.date_created = datetime.now()
        self.is_active = True
        print(f"Item {self.text} added with {self.amount} amount")

    def __repr__(self):
        return f"{self.id} => {self.user_id} => {self.text}"
