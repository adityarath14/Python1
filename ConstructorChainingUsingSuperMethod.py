class V1():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
class V2(V1):
    def __init__(self,name,gender,Aadhar,mno):
        super().__init__(name,gender)
        self.Aadhar=Aadhar
        self.mno=mno
obj=V2('Virat Kohali','Male',123456789,987654321)
print(obj.mno)
print(obj.Aadhar)