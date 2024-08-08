class Father():
    def skills(self):
        print('running')
        print('driving')
class Mother():
    def skills(self):
        print('cooking')
        print('scolding')
class Child(Father,Mother):
    def skills(self):
        Mother.skills(self)
        Father.skills(self)
        print('lazy')
        print('studying')
obj=Child()
obj.skills()