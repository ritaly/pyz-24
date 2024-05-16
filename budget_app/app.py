from flask import Flask, render_template

app = Flask(__name__)

class Expense:
    def __init__(self, description, amount, date=None):
        self.description = description
        self.amount = amount
        self.date = date


exp = Expense('Frige', 2000)
expenses_list = [exp]
@app.route('/')
def home():
    return render_template('index.html', expenses=expenses_list)


def create_expense():
    pass

def update_expense():
    pass

def delete_expense():
    pass


if __name__ == '__main__':
    app.run(debug=True)