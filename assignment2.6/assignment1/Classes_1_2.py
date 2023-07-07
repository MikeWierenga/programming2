"""
Author: Hannah Zantinge
Date: 03-04-2023
Description: This module contains several classes.
             -------------------------------------
             Atom : Represents an atom
             Molecule : Represents a molecule
             Chloroplast : Represents a chloroplast
"""

class Atom:
    """
    A class to represent an atom and provides methods
    to calculate proton number, mass number, and compare atoms.

    ...

    Attributes
    ----------
    symbol : str
        The letter symbol of the atom
    atomic_number : int
        The atomic number of the atom
    number_of_neutrons : int
        The number of neutron in the atom

    """
    
    def __init__(self, symbol, atomic_number, number_of_neutrons):
        """
        Class constructor with symbol, atomic_number and
        number_of_neutrons as attributes.
        """

        self.symbol = symbol
        self.atomic_number = atomic_number
        self.number_of_neutrons = number_of_neutrons

    def proton_number(self):
        """
        Calculates the proton number of the atom.
        """
        return self.atomic_number

    def mass_number(self):
        """
        Calculates the mass number of the atom.
        """
        mass_number = self.atomic_number + self.number_of_neutrons
        return mass_number

    def isotope(self, new_neutron):
        """
        Takes in a new amount of neutrons. Updates the number of
        neutrons.
        """
        self.number_of_neutrons = new_neutron
    
    def is_same_atom(self, first, second):
        """
        Takes in two atomic numbers. Raises an exception when the
        two numbers are not the same.
        """
        if  first != second:
            raise Exception("Not the same atom")

    def __eq__(self, other):
        """
        Overrides the default equality operator.
        """
        if isinstance(other, Atom):
            return self.atomic_number == other.atomic_number

    def __lt__(self, other):
        """
        Overrides the default less than operator.
        """
        if isinstance(other, Atom):
            Atom.is_same_atom(self, self.atomic_number, other.atomic_number)
            return self.number_of_neutrons < other.number_of_neutrons

    def __gt__(self, other):
        """
        Overrides the default greater than operator.
        """
        if isinstance(other, Atom):
            Atom.is_same_atom(self, self.atomic_number, other.atomic_number)
            return self.number_of_neutrons > other.number_of_neutrons
    
    def __le__(self, other):
        """
        Overrides the default less than or equal to operator.
        """
        if isinstance(other, Atom):
            Atom.is_same_atom(self, self.atomic_number, other.atomic_number)
            return self.number_of_neutrons <= other.number_of_neutrons

    def __ge__(self, other):
        """
        Overrides the default greater than or equal to operator.
        """
        if isinstance(other, Atom):
            Atom.is_same_atom(self, self.atomic_number, other.atomic_number)
            return self.number_of_neutrons >= other.number_of_neutrons
            
class Molecule:
    """
    A class to represent a molecule, generates molecule formulas,
    performs addition between molecules, and overrides the string representation.

    ...

    Attributes
    ----------
    atom_list : list
        A list of tuples. Each tuple contains an atom and an integer
        that represents the amount of the atom the molecule contains
    molecule_formula : string
        The molecule formula
    """

    def __init__(self, atom_list):
        """
        Class constructor with atom_list and molecule_formula as
        attributes.
        """
        self.atom_list = atom_list
        self.molecule_formula = Molecule.formula(self)
    
    def formula(self):
        """
        Returns the molecule formula in a string.
        """
        formula = ""
        for atoms in self.atom_list:
             atom, number = atoms
             formula += atom.symbol
             formula += str(number)
        return formula.replace("1", "")


    def __str__(self):
        """
        Returns the molecule formula as a string.
        """
        return self.molecule_formula

    def __add__(self, other):
        """
        Overrides the default addition operator.
        """
        if isinstance(other, Molecule):
            return Molecule(self.atom_list + other.atom_list)

class Chloroplast:
    """
    A class to represent a Chloroplast, tracks the amounts of water,
    CO2, sugar, and oxygen, performs photosynthesis by consuming molecules,
    and provides a string representation of its water and CO2 counts.

    ...

    Attributes
    ----------
    water : int
        Represents the amount of water molecules
    co2 : int
        Represents the amount of CO2 molecules
    sugar_amount : int
        Represents the amount of sugar that is produced
    oxygen_amount : int
        Represents the amount of oxygen that is produced
    """

    def __init__(self):
        """
        Class constructor with water, co2, sugar_amount, oxygen as
        attributes.
        """
        self.water = 0
        self.co2 = 0
        self.sugar_amount = 0
        self.oxygen_amount = 0
        

    def add_molecule(self, molecule):
        """
        Takes in a molecule, checks if the molecule is CO2 or H2O.
        Add 1 water to the watercount if it is H2O and add 1 water
        to the CO2 count if it is a CO2 molecule.
        """

        if molecule.molecule_formula not in ["CO2", "H2O"]:
            raise ValueError("Not CO2 or H2O")

        if molecule.molecule_formula == "H2O":
            self.water += 1
        elif molecule.molecule_formula == "CO2":
            
            self.co2 += 1
        if self.water >= 12 and self.co2 >= 6:
            print(self.photosynthesis())
            print("\n=== Photosynthesis!")
        else:
            return []
        

    
    def photosynthesis(self):
        """
        Performs photosynthesis by consuming water and CO2 molecules
        and producing sugar and oxygen molecules.
        """
        self.water -= 12
        self.co2 -= 6
        self.sugar_amount += 1
        self.oxygen_amount += 6
        oxygen = Molecule([(Atom("O", 8, 8) , 2)])
        sugar = Molecule([(Atom('C', 6, 6),6),(Atom('H', 1, 1), 12),(Atom("O", 8, 8), 6)])
        return [(sugar.__str__(), self.sugar_amount), (oxygen.__str__(), self.oxygen_amount)]
        
    
    def __str__(self):
        """
        Returns a string representation of the Chloroplast's water and CO2 counts.
        """
        return "water = {w}\nco2 = {c}".format(w = self.water, c = self.co2)
