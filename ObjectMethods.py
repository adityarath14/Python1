class M12:
    time='2:30'
    course='Python Full Stack'
    def __init__(self,name,mbno,gender,Aadhar):
        self.nm=name
        self.mbno=mbno
        self.gender=gender
        self.Aadhar=Aadhar
    def Details(self):
        print(f'name:{self.nm}')
        print(f'Mobile Number:{self.mbno}')
        print(f'Gender is:{self.gender}')
        print(f'Aadhar Number:{self.Aadhar}')
st1=M12('Ben10',8280952019,'MALE',123456)
st2=M12('Bheem',637172055,'MALE',789123)
st3=M12('Dora',6371111893,'FEMALE',456789)
st3.Details()
print('-'*20)
st1.Details()