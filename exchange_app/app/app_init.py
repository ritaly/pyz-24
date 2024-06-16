from flask import Flask

from .database import db
from .routes.product_routes import product_bp
from .routes.static_routes import static_bp


def create_app():
    app = Flask(__name__, static_folder='UI/static')
    app.config.from_object('config.Config')
    db.init_app(app)

    app.register_blueprint(static_bp, url_prefix='')
    app.register_blueprint(product_bp, url_prefix='/api/')

    with app.app_context():
        db.create_all()

    return app
