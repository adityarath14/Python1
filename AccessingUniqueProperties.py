class M12:
    time='2:30'
    course='Python Full Stack'
    def __init__(self,name,mbno,gender,Aadhar):
        self.nm=name
        self.mbno=mbno
        self.gender=gender
        self.Aadhar=Aadhar
st1=M12('BEN10',8280952019,'MALE',63952122)
st2=M12('Bheem',6371720557,'MALE',62011452)
st3=M12('Dora',6371111893,'FEMALE',9935201)
print(st3.nm,st3.mbno,st3.gender)
st3.nm='Heroine'
print(st2.nm,st2.mbno,st2.gender)
print(st3.nm,st3.mbno,st3.gender)