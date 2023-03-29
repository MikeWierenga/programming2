from Atom import Atom
from Molecule import Molecule

class Chloroplast:
    def __init__(self):
        self.water = 0
        self.co2 = 0

    def __str__(self):
        return f"there are {self.water} water molecules and {self.co2} co2 molecules present"

    def add_molecule(self, molecule: Molecule): 
        if molecule.__str__() not in ["H2O", "CO2"]:
            raise ValueError

        if molecule.__str__() == "H2O":
            self.water +=1

        if molecule.__str__() == "CO2":
            self.co2 +=1    

        if self.water >= 6 and self.co2 >= 12:
            return self.photosynthesis()
        
        return []

    def photosynthesis(self):
        self.water -= 6
        self.co2 -= 12
        
        hydrogen = Atom('H', 1, 1)
        carbon = Atom('C', 6, 6)
        oxygen = Atom('O', 8, 8)

        sugar = Molecule([(carbon, 6), (hydrogen, 12), (oxygen, 6)])
        oxygenM = Molecule([(oxygen, 2)])
        
        return [(sugar.__str__(), 1), (oxygenM.__str__(), 6)]

#testing
hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
demo = Chloroplast()
els = [water, co2]

while (True):
    print ('\nWhat molecule would you like to add?')
    print ('[1] Water')
    print ('[2] carbondioxyde')
    print ('Please enter your choice: ', end='')
    try:
        choice = int(input())
        res = demo.add_molecule(els[choice-1])
        if (len(res)==0):
            print (demo)
        else:
            print ('\n=== Photosynthesis!')
            print (res)
            print (demo)

    except Exception:
        print ('\n=== That is not a valid choice.')