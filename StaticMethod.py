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
    def deposite(self):
        amount=int(input('Enter Amount to Deposite:'))
        self.Bal+=amount
        print('Amount Credited Successfully.....')
        print(f'Avaiable Balance is {self.Bal}')
    def Withdraw(self):
        if self.pin==self.cpin():
            amount=int(input('Enter amount To Withdraw:'))
            if amount<=self.Bal:
                self.Bal-=amount
                print('Amount debited Successfully......')
                print(f'Avaiable Balance is {self.Bal}')
            else:
                print('Insufficient Funds....')
        else:
            print('Invalid Pin')
    @staticmethod
    def cpin():
        password=int(input('Enter The Pin :'))
        return password
us1=ourBank('Ambani',111111111,9856224562,1000,1111)
us2=ourBank('Tata',222222222,6322554499,1500,9999)
us2.Withdraw()