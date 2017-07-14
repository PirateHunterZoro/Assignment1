"""
Usage of inheritance
"""

class parent:
    balance=100
    def getbalance(self): return self.balance

class child(parent):
    def getbalance(self): print(super().getbalance())

if __name__ == "__main__":
    c=child()
    c.getbalance()