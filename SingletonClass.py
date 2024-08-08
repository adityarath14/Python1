def SingleTon(arg):
    L=[]
    def Inner():
        if len(L)==0:
            ob=arg()
            print(ob)
            L.append(ob)
        else:
            pass
    return Inner
@SingleTon
class PVR():
    def __init__(self):
        print('Object Created')
obj1=PVR()
obj2=PVR()
obj3=PVR()