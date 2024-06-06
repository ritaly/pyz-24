
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.routes.product_routes import product_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(product_bp, url_prefix='/api' )
    with app.app_context():
        db.create_all()

    return app