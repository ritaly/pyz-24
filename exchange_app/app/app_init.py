from flask import Flask, send_from_directory

from .database import db
from .routes.product_routes import product_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.route('/')
    def home():
        return send_from_directory('UI', 'index.html')

    app.register_blueprint(product_bp, url_prefix='/api/')

    with app.app_context():
        db.create_all()

    return app
