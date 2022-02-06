from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash

from riolists import app, db, User, Items


cli = FlaskGroup(app)


@cli.command("poke")
def poke_flask_app():
    """A test function to check the app is alive."""
    print("===\nUp and running, dude!\n===")


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(login="rioran", name="Rioran", password=generate_password_hash("rioran")))
    db.session.add(User(login="test", password=generate_password_hash("rioran")))
    db.session.add(Items(text="Tomatoes", amount=10))
    db.session.add(Items(text="Potatoes", amount=20))
    db.session.add(Items(text="Cucumbers", amount=7))
    db.session.commit()


if __name__ == "__main__":
    cli()
