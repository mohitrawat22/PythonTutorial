class Bank:
    def __init__(self, owner, value=0):
        self.value = value
        self.owner = owner
    
    def deposit(self, amount):
        self.value = self.value + amount

    def withdraw(self, amount):
        if self.value < amount:
            print('Funds unavailable')
        else:
            self.value = self.value - amount

acc1 = Bank('m1', 100)
acc2 = Bank('m2', 200)

print(acc1.value)
acc1.deposit(100)
acc1.withdraw(150)
acc1.withdraw(100)
print(acc1.value)
print(acc2.value)
