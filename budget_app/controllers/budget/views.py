from flask import Flask, flash, render_template, request, redirect, url_for

from controllers.budget import budget_bp
from models.budget_manager import BudgetManger, InvalidExpenseError, NotFoundExpenseError

budget_manager = BudgetManger()

@budget_bp.route('/')
def show_expenses():
    return render_template('budget.html', expenses=budget_manager.expenses)


@budget_bp.route('/add', methods=['GET', 'POST'])
def create_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = request.form['date']
        try:
            budget_manager.add_expense(description, amount, date)
            flash("Successfully created expense", "success")
            return redirect(url_for('budget.home'))
        except InvalidExpenseError as err:
            flash(f"{err}", "danger")

    return render_template('add.html')


@budget_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def update_expense(id):
    if request.method == 'GET':
        try:
            expense = budget_manager.get_expense(id)
            return render_template('edit.html', expense=expense)
        except NotFoundExpenseError as err:
            flash(f"{err}", "danger")
            return redirect(url_for('show_expenses'))

    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])
        date = request.form['date']
        try:
            budget_manager.update_expense(id, description, amount, date)
            flash("Successfully edited expense", "success")
            return redirect(url_for('home'))
        except InvalidExpenseError as err:
            flash(f"{err}", "danger")
            expense = budget_manager.get_expense(id)
            return render_template('edit.html', expense=expense)


@budget_bp.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    try:
        budget_manager.delete_expense(id)
        flash("Successfully deleted expense", "success")
    except InvalidExpenseError as err:
        flash(f"{err}", "danger")
    return redirect(url_for('show_expenses'))

