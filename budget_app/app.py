from flask import Flask, flash, render_template, request, redirect, url_for
from models.budget_manager import BudgetManger, InvalidExpenseError, NotFoundExpenseError

app = Flask(__name__)
app.secret_key = 'secret-key'
budget_manager = BudgetManger()

@app.route('/')
def home():
    return render_template('index.html', expenses=budget_manager.expenses)


@app.route('/add', methods=['GET', 'POST'])
def create_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = request.form['date']
        try:
            budget_manager.add_expense(description, amount, date)
            flash("Successfully created expense", "success")
            return redirect(url_for('home'))
        except InvalidExpenseError as err:
            flash(f"{err}", "error")

    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def update_expense(id):
    if request.method == 'GET':
        try:
            expense = budget_manager.get_expense(id)
            return render_template('edit.html', expense=expense)
        except NotFoundExpenseError as err:
            flash(f"{err}", "error")
            return redirect(url_for('home'))

    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = request.form['date']
        try:
            budget_manager.update_expense(id, description, amount, date)
            flash("Successfully edited expense", "success")
            return redirect(url_for('home'))
        except InvalidExpenseError as err:
            flash(f"{err}")
            expense = budget_manager.get_expense(id)
            return render_template('edit.html', expense=expense)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    try:
        budget_manager.delete_expense(id)
        flash("Successfully deleted expense", "success")
    except InvalidExpenseError as err:
        flash(f"{err}", "error")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
