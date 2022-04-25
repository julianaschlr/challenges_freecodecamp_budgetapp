def create_spend_chart(categories):
    lines = []
    line_funds = []
    total = []

    return None


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=""):

        d_list = {"amount": float(amount), "description": description}
        self.ledger.append(d_list)

    def withdraw(self, amount, description=""):

        if amount < self.get_balance():
            w_list = {"amount": float(amount) * -1, "description": description}
            self.ledger.append(w_list)
            return True
        else:
            return False

    def get_balance(self):

        current_balance = float()
        for key in self.ledger:
            value_in_key = key["amount"]
            current_balance += value_in_key
        return current_balance

    def transfer(self, amount, budget_category):

        if amount < self.get_balance():
            tw_list = {"amount": float(amount) * -1, "description": f"Transfer to {budget_category.name}"}
            self.ledger.append(tw_list)
            td_list = {"amount": float(amount), "description": f"Transfer from {self.name}"}
            budget_category.ledger.append(td_list)
            return True

        else:
            return False

    def check_funds(self, amount):

        if float(amount) > self.get_balance():
            return False

        else:
            return True
