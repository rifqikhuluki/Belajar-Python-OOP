class BankAccount:
    no = ""
    balance = 0
    active = True

    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance
    
    @classmethod
    def disable(cls, no, balance=0):
        result = cls(no, balance)
        result.active = False
        return result
    
bank_account1 = BankAccount("123235", 100000)
print(f"{bank_account1.no} - {bank_account1.balance} - {bank_account1.active}")

bank_account2 = BankAccount.disable("1325457", 100000)
print(f"{bank_account2.no} - {bank_account2.balance} - {bank_account2.active}")
