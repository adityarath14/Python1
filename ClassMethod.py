class ourBank:
    nob=1
    IFSC='OBI000420'
    roi=8
    def __init__(self,name,Aadhar,mno,Bal):
        self.name=name
        self.Aadhar=Aadhar
        self.mno=mno
        self.Bal=Bal
    def deposite(self):
        amount=int(input('Enter amount to deposite:'))
        self.Bal+=amount
        print('Amount Creadeted Successfully....')
        print(f'Avaiable Balance is {self.Bal}')
    def withdraw(self):
        amount=int(input('Enter Amount To withdraw:'))
        if amount<=self.Bal:
            self.Bal-=amount
            print('Amount debited successfully.....')
            print(f'Avaiable Balance is {self.Bal}')
        else:
            print('Insufficient Funds...')
    @classmethod
    def croi(cls):
        newv=float(input('enter new roi:'))
        cls.roi=newv
us1=ourBank('Ambani',111111111,986523456,1000)
us2=ourBank('TATA',22222222,632569955,1500)
print(ourBank.roi)
ourBank.croi()
print(us1.roi)
print(us2.roi)