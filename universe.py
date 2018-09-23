import random
import star
from star import Star
from star import DwarfStar
from star import GiantStar
from star import MediumStar


class Universe:
    def __init__(self):
        self.dwarf_Gaseous_Planets=0
        self.dwarf_Rocky_Planets=0
        self.dwarf_Habitable_Planets=0
        self.dwarf_Intelligent_Planets=0
        self.giant_Gaseous_Planets=0
        self.giant_Rocky_Planets=0
        self.giant_Habitable_Planets=0
        self.giant_Intelligent_Planets=0
        self.medium_Gaseous_Planets=0
        self.medium_Rocky_Planets=0
        self.medium_Habitable_Planets=0
        self.medium_Intelligent_Planets=0

        self.DwarfStars=[]
        self.GiantStars=[]
        self.MediumStars=[]

        kInput=input("Please enter the number of stars?") 
        self.no_of_stars= int(eval(kInput)) 
        print(self.no_of_stars)
        for i in range( 0, self.no_of_stars ):
            value=random.randint(1,3)
            if value == 1:
                star = DwarfStar()
                self.DwarfStars.append(star)

                self.dwarf_Gaseous_Planets=self.dwarf_Gaseous_Planets + len(star.GaseousPlanets)
                self.dwarf_Rocky_Planets=self.dwarf_Rocky_Planets + len(star.RockyPlanets)
                self.dwarf_Habitable_Planets=self.dwarf_Habitable_Planets + len(star.HabitablePlanets)
                self.dwarf_Intelligent_Planets=self.dwarf_Intelligent_Planets + star.IntellignetLifeCount

            elif value == 2:
                star= GiantStar()
                self.GiantStars.append(star)

                self.giant_Gaseous_Planets=self.giant_Gaseous_Planets + len(star.GaseousPlanets)
                self.giant_Rocky_Planets=self.giant_Rocky_Planets + len(star.RockyPlanets)
                self.giant_Habitable_Planets=self.giant_Habitable_Planets + len(star.HabitablePlanets)
                self.giant_Intelligent_Planets=self.giant_Intelligent_Planets + star.IntellignetLifeCount

        
            
            else:
                star= MediumStar()
                self.MediumStars.append(star)

                self.medium_Gaseous_Planets=self.medium_Gaseous_Planets + len(star.GaseousPlanets)
                self.medium_Rocky_Planets=self.medium_Rocky_Planets + len(star.RockyPlanets)
                self.medium_Habitable_Planets=self.medium_Habitable_Planets + len(star.HabitablePlanets)
                self.medium_Intelligent_Planets=self.medium_Intelligent_Planets + star.IntellignetLifeCount
               

    def printUniverse(self):
        print( "Total number of stars in  my universe", self.no_of_stars )
        print( "There are ", len(self.DwarfStars) , " Dwarf Stars with:" )
        print( "          ", self.dwarf_Gaseous_Planets , " Gaseous Planets" )
        print( "          ", self.dwarf_Rocky_Planets , " Rocky Planets" )
        print( "          ", self.dwarf_Habitable_Planets , " Habitable Planets" )
        print( "          ", self.dwarf_Intelligent_Planets, " Planets with Intelligent Life \n\n" ) 
        
        print( "There are ", len(self.GiantStars) , "Giant Stars with:" )
        print( "          ", self.giant_Gaseous_Planets , " Gaseous Planets" )
        print( "          ", self.giant_Rocky_Planets , " Rocky Planets" )
        print( "          ", self.giant_Habitable_Planets , " Habitable Planets" )
        print( "          ", self.giant_Intelligent_Planets, " Planets with Intelligent Life \n\n" )

        print( "There are ", len(self.MediumStars) , "Medium Stars with:" )
        print( "          ", self.medium_Gaseous_Planets , " Gaseous Planets" )
        print( "          ", self.medium_Rocky_Planets , " Rocky Planets" )
        print( "          ", self.medium_Habitable_Planets , " Habitable Planets" )
        print( "          ", self.medium_Intelligent_Planets, " Planets with Intelligent Life \n\n" )


        





          