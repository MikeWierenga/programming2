from Atom import Atom

class Molecule:
    def __init__(self, tupplelist):
        self.atoms = tupplelist

    def __str__(self):
        render = ""
        for atom in self.atoms:
            render += atom[0].atom_symbol
            if atom[1] > 1:
                render += str(atom[1])
        return render         
    
    
    def __add__(self, other):
        return Molecule(self.atoms + other.atoms)

hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
print (water) # H2O
print (co2) # CO2
print (water + co2) # H2OCO2