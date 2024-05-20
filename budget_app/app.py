from flask import Flask, render_template, request, redirect, url_for
from models.budget_manager import BudgetManger

app = Flask(__name__)
budget_manager = BudgetManger()

@app.route('/')
def home():
    return render_template('index.html', expenses=budget_manager.expenses)


@app.route('/add', methods=['GET', 'POST'])
def create_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        budget_manager.add_expense(description, amount,date)

        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def update_expense(id):
    if request.method == 'GET':
        expense = budget_manager.get_expense(id)
        return render_template('edit.html', expense=expense)

    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        budget_manager.update_expense(id, description, amount, date)
        return redirect(url_for('home'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    budget_manager.delete_expense(id)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
