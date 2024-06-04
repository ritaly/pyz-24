from flask import Flask
from database import db
from controllers.budget.views import budget_bp

app = Flask(__name__)
app.secret_key = 'secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(budget_bp)


@app.route('/')
@app.route('/index')
def home():
    # TODO: add index.html template
    return 'Hello hello!'


if __name__ == '__main__':
    app.run(debug=True)
