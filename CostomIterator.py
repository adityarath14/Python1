class numbers:
    def __init__(self,sv,ev):
        self.sv=sv
        self.ev=ev
    def __iter__(self):
        return self
    def __next__(self):
        num=self.sv
        if self.sv==self.ev+1:
            raise StopIteration
        self.sv+=1
        return num
obj=numbers(11,15)
itobj=iter(obj)
print(next(itobj))
print(next(itobj))
print(next(itobj))
print(next(itobj))
print(next(itobj))
print(next(itobj))