from flask.cli import FlaskGroup

from riolists import app, db


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


if __name__ == "__main__":
    cli()

