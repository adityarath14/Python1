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
            print('Ticktes Booked Successfully')
            self.Maxtick-=reqtick
            print(f'Avaiable Ticktes are {self.Maxtick}')
        else:
            print('Ticket Not Avaiable')
def Bmys():
    obj=Kalki()
    NOT=int(input('Enter The Number Of Ticktes:'))
    obj.booking(NOT)
user1=Bmys()
user2=Bmys()