class Atom:
    def __init__(self, atom_symbol, atom_number, number_of_neutrons):
        self.atom_symbol = atom_symbol
        self.atom_number = atom_number
        self.number_of_neutrons = number_of_neutrons

    def proton_number(self):
        return self.atom_number

    def mass_number(self):
        return self.atom_number + self.number_of_neutrons    

    def isotope(self, isotope):
        self.number_of_neutrons = isotope

    def check_validity(self, other):
        if not isinstance(self, Atom) or not isinstance(other, Atom):
            raise TypeError()
        if self.atom_number != other.atom_number:
            raise Exception

    def __lt__(self, other):
        self.check_validity(other)
        return self.mass_number() < other.mass_number()

    def __le__(self, other):
        self.check_validity(other)
        return self.mass_number() <= other.mass_number()

    def __ge__(self, other):
        self.check_validity(other)
        return not self <= other

    def __gt__(self, other):
        self.check_validity(other)
        return not self < other

    def __eq__(self, other):
        self.check_validity(other)
        return self.mass_number() == other.mass_number()    
  
protium = Atom('H', 1, 1)
deuterium = Atom('H', 1, 2)
oxygen = Atom('O', 8, 8)
tritium = Atom('H', 1, 2)
tritium.isotope(3)

assert tritium.number_of_neutrons == 3
assert tritium.mass_number() == 4
assert protium < deuterium
assert deuterium <= tritium
assert tritium >= protium
# print (oxygen > tritium) # <-- this should raise an Exception