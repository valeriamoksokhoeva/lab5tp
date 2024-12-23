from abc import ABC, abstractmethod
class Sports(ABC):
    @abstractmethod
    def workout(self):
        pass

class Swimming(Sports):
    def workout(self):
        print('Swimming...', end=' ')

class Athletics(Sports):
    def workout(self):
        print('Running...', end=' ')

class WorkoutPlace(ABC):
    def __init__(self, sport: Sports):
        self.sport = sport
    @abstractmethod
    def place(self):
        pass

class SwimPlace(WorkoutPlace):
    def place(self):
        self.sport.workout()
        print('in the pool!')
class AthleticsPlace(WorkoutPlace):
    def place(self):
        self.sport.workout()
        print('in the stadium!')

swimming = Swimming()
athletics = Athletics()

swim_place = SwimPlace(swimming)
athletics_place = AthleticsPlace(athletics)

swim_place.place()        
athletics_place.place()   

