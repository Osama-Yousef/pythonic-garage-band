
from abc import abstractmethod, ABC

class Band():
    members = []
    bands = []
    def __init__(self,name):
        self.name=name
        Band.bands.append(self)

    def add_members(self,mname):
        self.mname=mname
        Band.members.append(mname)

    def play_solos(self):
        result =''
        for i in Band.members:
            result+= f'{i.play_solo()}\n'
        return result

    def to_list(self,cls):
        print(f"members of the {cls.bands} are {cls.members}")

    def __str__(self):
        return f"Band <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "
    
class Musician():
        
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def __str__(self):
        return f"Musician <{self.name}>"

    @abstractmethod
    def __repr__(self):
        return f" '{self.name}' "
    
    def play_solo(self):
        return f'{self.name} Play solo'

class Guitarist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"Guitarist <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "
    
    def get_instrument(self):
        return 'Guitarist'
    

class Bassist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"Bassist <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "

    def get_instrument(self):
        return 'Bassist'
    

class Drummer(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"Drummer <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "

    def get_instrument(self):
        return 'Drummer'

if __name__ == "__main__":
    john = Bassist('john')
    mike = Guitarist('mike')
    carlos = Drummer('carlos')

    print(john.get_instrument())
    print(mike.get_instrument())
    print(carlos.get_instrument())
    print(john.play_solo())
    print(mike.play_solo())
    print(carlos.play_solo())
   





