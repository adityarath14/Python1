class GrandMother:
    def __init__(self):
        print('GrandMother Properties')
class Father(GrandMother):
    def __init__(self):
        super().__init__()
        print('Father Properties')
class Child(Father):
    def __init__(self):
        Father.__init__(self)
        print('Chid Properties')
class GrandChild(Child):
    def __init__(self):
        Child.__init__(self)
        print('Grandchild Properties')
obj=GrandChild()