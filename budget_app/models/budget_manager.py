from expense import Expense
class BudgetManger:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self, description, amount, date):
        new_expense = Expense(self.next_id, description, amount, date)
        self.expenses.append(new_expense)
        self.next_id += 1



    def update_expense(self, id, description, amount, date):
        expense = self.get_expense(id)
        if expense:
            expense.description = description
            expense.amount = amount
            expense.date = date


    def get_expense(self, id):
        for exp in self.expenses:
            if exp.id == id:
                return exp

        return None