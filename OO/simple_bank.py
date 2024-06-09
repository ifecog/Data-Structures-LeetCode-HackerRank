class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.n = len(balance)
        
    
    def transfer(self, account1, account2, money):
        if account1 in range(1, self.n + 1) and account2 in range(1, self.n + 1):
            if self.balance[account1 - 1] >= money:
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
                return True
        
        return False
    
    
    def deposit(self, account, money):
        if account in range(self.n + 1):
            self.balance[account - 1] += money
            return True
        
        return False
    
    
    def withdraw(self, account, money):
        if account in range(self.n + 1):
            if self.balance[account - 1] >= money:
                self.balance[account - 1] -= money
                return True
        
        return False