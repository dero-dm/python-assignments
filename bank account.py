class BankAccount:
    def __init__(self,balance,name,number):
       self.__balance = balance
       self.name = name
       self._number = number
    def deposit(self,amount):
        self.__balance += amount
        return f"DEPOSITED {amount}"
    def get_balance(self):
         
         return self.__balance
account = BankAccount(1500,"John",254)
#print(account.__balance)
print(account.name)
print(account._number)

print(account.deposit(2000))
print(account.get_balance())                        