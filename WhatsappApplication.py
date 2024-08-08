class wppv1:
    def __init__(self,mno,name,dp):
        self.mno=mno
        self.name=name
        self.dp=dp
    def Details(self):
        print(f'{self.mno}')
        print(f'{self.name}')
        print(f'{self.dp}')
class wppv2(wppv1):
    def __init__(self,mno,name,dp,audiocall,status,vmsg):
        super().__init__(mno,name,dp)
        self.audiocall=audiocall
        self.status=status
        self.vmsg=vmsg
    def Details(self):
        super().Details()
        print(f'{self.audiocall}')
        print(f'{self.status}')
        print(f'{self.vmsg}')
class wppv3(wppv2):
    def __init__(self,mno,name,dp,audiocall,status,vmsg,videocall,Business,channel):
        super().__init__(mno,name,dp,audiocall,status,vmsg)
        self.videocall=videocall
        self.Business=Business
        self.channel=channel
    def Details(self):
        super().Details()
        print(f'{self.videocall}')
        print(f'{self.Business}')
        print(f'{self.channel}')
user1=wppv1(8280952019,'Aditya','Given')
user1.Details()
print('-'*20)
user2=wppv2(9938203635,'Gadadhar','Given','Yes','Yes','yes')
user2.Details()
print('-'*20)
user3=wppv3(6371720557,'Adi','Notgiven','yes','yes','yes','yes','yes','yes')
user3.Details()