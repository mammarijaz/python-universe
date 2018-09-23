from universe import Universe
from probe import Probe

def main ():
 u1=Universe()
 u1.printUniverse()

 stars=u1.DwarfStars + u1.GiantStars + u1.MediumStars

 p1=Probe(stars)
 p1.printProbe()


if __name__=="__main__":
    main()