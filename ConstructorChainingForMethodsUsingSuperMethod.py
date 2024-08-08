class V1():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def Details(self):
        print(f'Name={self.name}')
        print(f'Gender={self.gender}')
class V2(V1):
    def __init__(self,name,gender,Aadhar,mno):
        super().__init__(name,gender)
        self.Aadhar=Aadhar
        self.mno=mno
    def details(self):
        super().Details()
        print(f'Aadhar={self.Aadhar}')
        print(f'mno={self.mno}')
obj1=V2('Virat Kohali','Male',123456789,987654321)
obj2=V2('MS Dhoni','Male',1523648925,93625987422)
obj2.details()