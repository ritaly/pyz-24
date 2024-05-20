from .expense import Expense


class InvalidExpenseError(Exception):
    pass

class NotFoundExpenseError(Exception):
    pass

class BudgetManger:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self, description, amount, date):
        if not description or amount <= 0:
            raise InvalidExpenseError("Invalid expense data")
        new_expense = Expense(self.next_id, description, amount, date)
        self.expenses.append(new_expense)
        self.next_id += 1

    def update_expense(self, id, description, amount, date):
        expense = self.get_expense(id)
        if not description or amount <= 0:
            raise InvalidExpenseError("Invalid expense data")
        if expense:
            expense.description = description
            expense.amount = amount
            expense.date = date

    def delete_expense(self, id):
        expense = self.get_expense(id)
        if expense:
            self.expenses.remove(expense)

    def get_expense(self, id):
        for exp in self.expenses:
            if exp.id == id:
                return exp
        raise NotFoundExpenseError(f"Expense ID = {id} not found")