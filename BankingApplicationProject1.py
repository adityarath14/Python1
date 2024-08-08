class ourBank:
    nob=1
    IFSC='OBI000420'
    roi=8
    def __init__(self,name,Aadhar,mno,Bal,pin):
        self.name=name
        self.Aadhar=Aadhar
        self.mno=mno
        self.Bal=Bal
        self.pin=pin
    def CheckBalance(self):
        if self.pin==self.takepin():
            print(f'Avaiable Balance is {self.Bal}')
        else:
            print('Invalid pin')
    def deposite(self):
        if self.pin==self.takepin():
            amount=int(input('Enter Amount to deposite:'))
            self.Bal+=amount
            print('Amount Credited Successfully.....')
            print(f'Avaiable Balance is {self.Bal}')
        else:
            print('Invalid Pin')
    @classmethod
    def croi(cls):
        newv=float(input('enter new roi:'))
        cls.roi=newv
    def withdraw(self):
        if self.pin==self.takepin():
            amount=int(input('Enter Amount to withdraw:'))
            if amount<=self.Bal:
                self.Bal-=amount
                print('Amount Debited Successfully.....')
                print(f'Avaiable Balance is {self.Bal}')
            else:
                print('Insufficient Fund')
        else:
            print('Invalid Pin')
    @staticmethod
    def takepin():
        password=int(input('Enter the pin:'))
        return password
us1=ourBank('Ambani',111111,9938546214,1000,1111)
us2=ourBank('Tata',2222222,9853621545,2000,9999)
us2.withdraw()
print('-'*20)
us1.CheckBalance()