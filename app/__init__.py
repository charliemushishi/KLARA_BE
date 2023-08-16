import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #Uncomment and configure the appropriate environment variables for your deployment for testing
    #app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("RENDER_EMOTE_URI")

    #Uncomment and configure the appropriate environment variables for your deployment for Auth
    #password = os.environ.get("DATABASE_PASSWORD")
    #username = os.environ.get("AUTH_USERNAME")

    #Import models here for Alembic setup
    from app.models.emotes import Emote

    db.init_app(app)
    migrate.init_app(app, db)

    #Register Blueprints here
    from .routes.emote_routes import emotes_bp
    app.register_blueprint(emotes_bp)

    #Uncomment and configure authentication as needed
    #app.jinja_env.globals.update(requires_auth=auth_decorator)

    CORS(app)
    return app
