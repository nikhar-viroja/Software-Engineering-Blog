class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient funds")
        else:
            self.__balance -= amount

my_account = BankAccount(1000)
my_account.deposit(500)
my_account.withdraw(200)
print(my_account.__balance) # this will result in an AttributeError since __balance is a private attribute