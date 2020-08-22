
from abc import abstractmethod

class Band:
    ''' class which creates band instances'''

    members = []

    class Musician():
    
        def __init__(self,name):
            self.name = name
            Band.members.append(self.name)
        
        @classmethod
        ##  Prints str of band members who play solo

        def play_solos(self):
            result = ''
            for i in Band.members:
                result += f'{i} play a solos\n'
            return result
        
        @abstractmethod
            ## will Return band name 

        def __str__(self):
            return f"Musician <{self.name}>"
        
        @abstractmethod
        def __repr__(self):
            return f" '{self.name}' "
        @classmethod
        # Returns all Band instances from members list

        def to_list(self):
            return Band.members
    
    ###  From Musician class, creates guitarist class

    class Guitarist(Musician):
        
        def __init__(self,name):
            super().__init__(name)

        def __str__(self):
            return f"Guitarist <{self.name}>"
        
        def __repr__(self):
            return f" '{self.name}' "
        
        def get_instrument(self):
            return 'Guitarist'
        
        def play_solo(self):
            return 'Play Guitar'
    
    ####  From Musician class, creates Bassist class

    class Bassist(Musician):
        
        def __init__(self,name):
            super().__init__(name)
        
        def __str__(self):
            return f"Bassist <{self.name}>"
        
        def __repr__(self):
            return f" '{self.name}' "
        
        def get_instrument(self):
            return 'Bassist'
        
        def play_solo(self):
            return 'Play Bassist'
    
    ###  From Musician class, creates Bassist class

    class Drummer(Musician):
        
        def __init__(self,name):
            super().__init__(name)
        
        def __str__(self):
            return f"Drummer <{self.name}>"
        
        def __repr__(self):
            return f" '{self.name}' "
        
        def get_instrument(self):
            return 'Drummer'
        
        def play_solo(self):
            return 'play drummer'


## the execution will be here 
if __name__ == "__main__":
    john = Band.Bassist('john')
    mike = Band.Guitarist('mike')
    carlos = Band.Drummer('carlos')




    print(mike.play_solos())


    print(Band.members)
