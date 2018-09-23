import random

class Planet:
    def __init__(self,type,intelligentLife):
      self.distance=random.randint(1,300)
      self.type=type
      self.intelligentLife=intelligentLife
      self.uniqueID=type + str( random.randint(1,30000) ) 

class RockyPlanet(Planet):      
    def __init__(self):  
      super().__init__('r',False)

class GaseousPlanet(Planet):  
    def __init__(self):  
      super().__init__('g',False)

class HabitablePlanet(Planet):  
    def __init__(self,start_zone,end_zone):  
      super().__init__('h',False)
      if (self.distance > start_zone and self.distance < end_zone):
         self.intelligentLife=True  
