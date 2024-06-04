from flask import render_template

from controllers.budget import budget_bp
from models.budget_manager import BudgetManger

budget_manager = BudgetManger()

@budget_bp.route('/')
def home():
    return render_template('index.html', expenses=budget_manager.expenses)


# create_expence

# read expence (single expence view)

# update_expence

# delete expence

