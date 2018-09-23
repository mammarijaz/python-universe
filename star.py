import random
import planet
from planet import Planet
from planet import RockyPlanet
from planet import GaseousPlanet
from planet import HabitablePlanet


class Star:
    def __init__(self):
      self.x = random.randint(2**3,2**64)
      self.y = random.randint(2**3,2**64)
      self.z = random.randint(2**3,2**64)
      self.RockyPlanets=[]
      self.GaseousPlanets=[]
      self.HabitablePlanets=[]
      self.IntellignetLifeCount=0
    
    def generatePlanets(self,maxNumber,start_zone,end_zone):
        for i in range( 1, maxNumber ):
            value=random.randint(1,3)
            if value == 1:
                p = RockyPlanet()
                self.RockyPlanets.append(p)
            
            elif value == 2:
                p= GaseousPlanet()
                self.GaseousPlanets.append(p)
            
            else:
                p= HabitablePlanet(start_zone,end_zone)
                self.HabitablePlanets.append(p)
                if(p.intelligentLife== True):
                    self.IntellignetLifeCount=self.IntellignetLifeCount + 1


class DwarfStar(Star):
    __chances_of_life=0.0006
    __range_of_planets=range(8,15)
    __goldilocks_zone_start=30
    __goldilocks_zone_end=90
    __recharge_amount=2**20

    def __init__(self):
        super().__init__()
        self.generatePlanets()


    def generatePlanets(self):
        maxNumberOfPlanets=random.randint(8,15)
        super().generatePlanets(maxNumberOfPlanets,self.__goldilocks_zone_start,self.__goldilocks_zone_end)

    def getRechargeAmount(self):
        return self.__recharge_amount



class GiantStar(Star):
    __chances_of_life=0.0005
    __range_of_planets=range(5,10)
    __goldilocks_zone_start=100
    __goldilocks_zone_end=250
    __recharge_amount=2**30    

    def __init__(self):
        super().__init__()
        self.generatePlanets()


    def generatePlanets(self):
        maxNumberOfPlanets=random.randint(5,10)
        super().generatePlanets(maxNumberOfPlanets,self.__goldilocks_zone_start,self.__goldilocks_zone_end)
    
    def getRechargeAmount(self):
        return self.__recharge_amount

class MediumStar(Star):
    __chances_of_life=0.0009
    __range_of_planets=range(2,9)
    __goldilocks_zone_start=60
    __goldilocks_zone_end=140
    __recharge_amount=2**25

    def __init__(self):
        super().__init__()
        self.generatePlanets()


    def generatePlanets(self):
        maxNumberOfPlanets=random.randint(2,9)
        super().generatePlanets(maxNumberOfPlanets,self.__goldilocks_zone_start,self.__goldilocks_zone_end)

    def getRechargeAmount(self):
        return self.__recharge_amount