#  Example work out for Bank Account
class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.__balance = balance
        
    def showBalance(self):
        print(f'{self.account_name}, your balance is {self.__balance}')
    
    def deposit(self, amount):
        self.__balance += amount
        self.showBalance()
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient balance!!!')
            return
        self.__balance -= amount
        self.showBalance()
        
    def transfer(self, amount):
        if amount > self.__balance:
            print('Insufficient balance!!!')
            return
        self.__balance -= amount
        return amount
        
siddharthBank_bimal = BankAccount('Bimal Regmi')
# siddharthBank_bimal.showBalance()     # 0
siddharthBank_bimal.deposit(3000)     # 3000
# siddharthBank_bimal.withdraw(2000)    # 1000
# siddharthBank_bimal.withdraw(2000)    # insuffi..
# siddharthBank_bimal.showBalance()     # 1000

siddharthBank_rajiv = BankAccount('Rajiv Yadav')
# siddharthBank_rajiv.showBalance()     # 0
siddharthBank_rajiv.deposit(30000000)     # 3000
# siddharthBank_rajiv.withdraw(20000)    # 1000
# siddharthBank_rajiv.withdraw(200000)    # insuffi..
# siddharthBank_rajiv.showBalance()     # 1000

siddharthBank_bimal.showBalance()
siddharthBank_rajiv.showBalance()
siddharthBank_bimal.deposit(siddharthBank_rajiv.transfer(100000))
# siddharthBank_bimal.showBalance()
siddharthBank_rajiv.showBalance()


prabhuBank = BankAccount