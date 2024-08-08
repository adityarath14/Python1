class RBI():
    def __init__(self,name,mno,bal):
        self.name=name
        self.mno=mno
        self.bal=bal
    def withdraw(self):
        amount=int(input('Enter amount to withdraw:'))
        if amount<=self.bal:
            self.bal-=amount
            print('Amount Withdraw Successfully')
        else:
            print('Insufficient funds----')
class SBI(RBI):
    def deposite(self):
        amount=int(input('Enter amount to deposite:'))
        self.bal+=amount
        print(f'Avaiable Balance is {self.bal}')
class HDFC(RBI):
    def deposite(self):
        amount=int(input('Enter amount to deposite:'))
        self.bal+=amount
        print(f'Avaiable Balance is {self.bal}')
obj1=SBI('Aditya',8280952019,1500)
obj1.withdraw()
obj2=HDFC('Ram',6371720557,1800)
obj2.withdraw()