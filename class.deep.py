class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("------")
# my_account.amount = 10000000
# my_account.owner = "Martin"
# my_account.__amount = 10000000
# my_account.get_balance()
