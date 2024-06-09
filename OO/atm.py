class ATM:
    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.banknotes = [0] * 5
        
        
    def deposit(self, banknotesCount):
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]
            
    
    def withdraw(self, amount):
        withdraw_count = [0] * 5
        
        # Try to withdraw from the largest denomination to the smallest
        for i in range(4, -1, -1):
            # Check if the current denomination can be used for the amount
            if amount >= self.denominations[i]:
                # Calculate the number of banknotes needed for the current denomination
                needed = amount // self.denominations[i]
                
                if needed <= self.banknotes[i]:
                    withdraw_count[i] = needed
                else:
                    withdraw_count[i] = self.banknotes[i]
                
                amount -= withdraw_count[i] * self.denominations[i]
        
        # Check if the entire amount has been withdrawn
        if amount == 0:
            # Update the ATM banknotes by subracting the withdrawn banknotes
            for i in range(5):
                self.banknotes[i] -= withdraw_count[i]
            return withdraw_count
        
        return [-1]
        