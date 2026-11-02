class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = [] # list to store transactions


    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self, amount, description='')
        if
        self.ledger.append({'amount': amount, 'description': description})
