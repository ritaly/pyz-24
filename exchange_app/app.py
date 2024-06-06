from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config.Config')
db = SQLAlchemy()
db.init_app(app)

@app.route('/')
def home():
    return '<h1>Hello</h1>'


if __name__ == '__main__':
    app.run(debug=True)