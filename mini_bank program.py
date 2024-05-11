class Bank:
    def __init__(self, account_no, owner_name, balance):
        self.account_no = account_no
        self.owner_name = owner_name
        self.balance = balance
    def widthdraw(self, amount):
        self.balance -= amount
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def current_balance(self):
        return self.balance
person=Bank(1234, 'John', 1000)
print(person.widthdraw(100))
print(person.deposit(100))
print(person.current_balance())