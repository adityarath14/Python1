def SingleTon(arg):
    L=[]
    def Inner():
        if len(L)==0:
            L.append(arg())
        return L[0]
    return Inner
@SingleTon
class Kalki():
    def __init__(self):
        self.Maxtick=200
    def booking(self,reqtick):
        if reqtick<=self.Maxtick:
            print('Ticket Booked Successfully')
            self.Maxtick-=reqtick
            print(f'Avaiable Ticktes are:{self.Maxtick}')
        else:
            print('Ticket Not Avaiable')
@SingleTon
class Deadpool():
    def __init__(self):
        self.Maxtick=150
    def booking(self,reqtick):
        if reqtick<=self.Maxtick:
            print('Ticket Booked Successfully')
            self.Maxtick-=reqtick
            print(f'Avaiable Ticktes are:{self.Maxtick}')
        else:
            print('Ticket Not Avaiable')
@SingleTon
class Pushpa2():
    def __init__(self):
        self.Maxtick=250
    def booking(self,reqtick):
        if reqtick<=self.Maxtick:
            print('Ticket Booked Successfully')
            self.Maxtick-=reqtick
            print(f'Avaiable Ticktes are:{self.Maxtick}')
        else:
            print('Ticket Not Avaiable')
def Bmys():
    print('1)Kalki\n2)Deadpool\n3)Pushpa2')
    choice=int(input('Enter The Choice Of Above Movie:'))
    if choice==1:
        obj=Kalki()
        NOT=int(input('Enter The Number Of Tickets:'))
        obj.booking(NOT)
    elif choice==2:
        obj=Deadpool()
        NOT=int(input('Enter The Number oF Ticktes:'))
        obj.booking(NOT)
    elif choice==3:
        obj=Pushpa2()
        NOT=int(input('Enter The Number oF Ticktes:'))
        obj.booking(NOT)
    else:
        print('No Choice Avaiable')
def PayTM():
    print('1)Kalki\n2)Deadpool\n3)Pushpa2')
    choice=int(input('Enter The Choice Of Above Movie:'))
    if choice==1:
        obj=Kalki()
        NOT=int(input('Enter The Number Of Tickets:'))
        obj.booking(NOT)
    elif choice==2:
        obj=Deadpool()
        NOT=int(input('Enter The Number oF Ticktes:'))
        obj.booking(NOT)
    elif choice==3:
        obj=Pushpa2()
        NOT=int(input('Enter The Number oF Ticktes:'))
        obj.booking(NOT)
    else:
        print('No Choice Avaiable')
user1=Bmys()
user2=PayTM()
user3=Bmys()
user4=PayTM()
user5=Bmys()