from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)  # Initialize SQLAlchemy app inside create_app

    migrate.init_app(app, db)

    from app.scheduler import start_scheduler  # Import here to avoid circular import

    start_scheduler(app)  # Call the scheduler setup function directly

    from app.routes import main_blueprint

    app.register_blueprint(main_blueprint)

    return app


# Import db after create_app to avoid circular import
from app.models import Event  # Example import to illustrate
