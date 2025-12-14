class BankAccount:

    __no = ""
    __balance = 0

    def __init__(self, no):
        self.__no = no

    @property
    def no(self):
        return self.__no
    
    @property
    def balance(self):
        return self.__balance
    
    def topup(self, topup):
        self.__balance += topup
    
    def checkout(self, checkout):
        if checkout > self.__balance:
            raise ValueError("Rekeningmu kurangg gook")
        else:
            self.__balance -= checkout

account1 = BankAccount("yadi122")
print(account1.no)
print(account1.balance)

# account1.no = "gk iso"

account1.topup(100000)
print(account1.balance)

account1.checkout(40000)
print(account1.balance)