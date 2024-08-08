class ourBank:
    nob=1
    IFSC='OBI000420'
    def __init__(self,name,Aadhar,mno,bal):
        self.name=name
        self.Aadhar=Aadhar
        self.mno=mno
        self.bal=bal
    def Deposite(self):
        amount=int(input('Enter your Deposite Amount:'))
        self.bal+=amount
        print('Amount Creadited Successfully.........')
        print(f'Avaiable Balance is :{self.bal}')
    def Withdraw(self):
        amount=int(input('Enter Amount to Withdraw:'))
        if amount<=self.bal:
            self.bal-=amount
            print('Amount Debitated Successfully........')
            print(f'Avaiable Balance is:{self.bal}')
        else:
            print('Insufficient Funds.....')
us1=ourBank('AMBANI',1111111,983215642,1000)
us2=ourBank('TATA',22222222,6325487922,2000)
us3=ourBank('AADHANI',3333333,9956231578,1500)
us4=ourBank('MALYA',44444444,9365214588,4200)
us3.Withdraw()