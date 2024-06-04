from flask import Flask

from controllers.budget import budget_bp

app = Flask(__name__)
app.secret_key = 'secret-key'

app.register_blueprint(budget_bp)


@app.route('/')
@app.route('/index')
def home():
    return 'Hello hello!'


if __name__ == '__main__':
    app.run(debug=True)
