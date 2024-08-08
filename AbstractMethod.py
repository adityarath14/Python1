from abc import ABC,abstractmethod
class RE(ABC):
    @abstractmethod
    def cc(self):
        pass
    def gear(self):
        print('5 Gears')
class classic(RE):
    def cc(self):
        print('350cc')
class GT(RE):
    def cc(self):
        print('650cc')
class Himalayan(RE):
    def cc(self):
        print('452cc')
obj1=classic()
obj1.gear()
obj2=GT()
obj2.cc()