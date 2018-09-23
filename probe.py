import math

class Probe:
    def __init__(self,stars):
        self.fuel=10**25
        self.x= 7646
        self.y= 72356
        self.z= 46508
        self.x1= 7646
        self.y1= 72356
        self.z1= 46508
        self.stars=stars
        self.distance=0
        self.stars_visited=[]
        self.planets_explored=0
        self.planet=self.explore()

    def explore(self):
        tempDistance=[]
        tempStars={}
        for star in self.stars:
            distance=math.sqrt( ( (self.x1 - star.x )**2 ) + ( (self.y1 - star.y )**2) + ( (self.z1 - star.z )**2) ) 
            tempDistance.append(distance)
            tempStars[distance]=star
        minDistance=min(tempDistance)
        star=tempStars[minDistance]
        if star not in self.stars_visited :    
            self.stars_visited.append(star)
            self.fuel=self.fuel - (minDistance*(10**6)) + star.getRechargeAmount()
            self.distance=self.distance + minDistance
            if self.fuel <= 0:
               self.fuel=0 
               return 0
            for planet in star.HabitablePlanets:
                self.planets_explored=self.planets_explored + 1;
                if planet.intelligentLife == True :
                   return planet.uniqueID
        self.x1= star.x
        self.y1= star.y
        self.z1= star.z
        self.explore()           


    def printProbe(self):
         print( "=============\n\n" )
         print( "Your origin was (", self.x ,",", self.y , ",",self.z,")" )
         print( "Traveled", self.distance * (10**6) )
         if self.fuel > 0:
            print( "        You have ", self.fuel," fuel remaining" )
         else:
            print( " You have run out of fuel" )    
         
         print( "        Visited ", len(self.stars_visited)," stars" )
         print( "        Explored ",self.planets_explored ," planets" )   
         if self.planets_explored > 0:   
            print( "        Found life on ",self.planet)
         else:   
            print( " Found no life" )  
             
              




        
        


