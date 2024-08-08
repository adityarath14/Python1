def SingleTon(arg):
    L=[]
    def Inner():
        if len(L)==0:
            ob=arg()
            L.append(ob)
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
def Bmys():
    print('1)Kalki\n2)Deadpool')
    choice=int(input('Enter The Choice Of Above Movie:'))
    if choice==1:
        obj=Kalki()
        NOT=int(input('Enter The Number Of Tickets:'))
        obj.booking(NOT)
    elif choice==2:
        obj=Deadpool()
        NOT=int(input('Enter The Number oF Ticktes:'))
        obj.booking(NOT)
    else:
        print('No Choice Avaiable')
user1=Bmys()
user2=Bmys()
user3=Bmys()
user4=Bmys()
user5=Bmys()