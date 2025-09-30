'''
J Austin Hutchinson
CSE 111
Week #
Assignment Name
'''
'''
I have added a calculation for how many elements are from each block of the periodic table
'''
from formula import parse_formula

def main():
    '''
    FOR: handling user input
        gets chemical formula
        gets sample mass in grams
        parses formula to components 
        calculates total molar mass based on the formula
        display molar mass
        calculate moles in sample
        display number of moles in sample.
    PARAM:  x
    RETURN: nothing
    '''
    formula = input("Enter the molecular formula of the sample: ")
    sample_size = float(input("Enter the mass in grams of the sample: "))

    periodic_table_dict = make_periodic_table()

    formula_list = parse_formula(formula,periodic_table_dict)

    molar_mass = compute_molar_mass(formula_list,periodic_table_dict)
    print(f"{molar_mass:.5f} grams/mole")

    sample_total_moles = sample_size/molar_mass
    print(f"{sample_total_moles:.5f} moles")

    sample_element_blocks = get_sample_element_blocks(formula_list,periodic_table_dict)
    for block, quantity in sample_element_blocks.items():
        if quantity > 1:
            print(f"The Sample has {quantity} elements from block {block}")
        else:
            print(f"The Sample has {quantity} element from block {block}")

    return 0

# Helper Functions
def make_periodic_table():
    '''
    FOR:    to create a dictionary containing the periodc table 
    PARAM:  none
    RETURN: dict of elements
    '''
    table = {# symbol: [name, atomic_mass]
        "Ac":	[ "Actinium",       227,        "f" ],
        "Ag":	[ "Silver",         107.8682,   "d" ],
        "Al":	[ "Aluminum",       26.9815386, "p" ],
        "Ar":	[ "Argon",          39.948,     "p" ],
        "As":	[ "Arsenic",	    74.9216,    "p" ],
        "At":	[ "Astatine",	    210,        "p" ],
        "Au":	[ "Gold",	        196.966569, "d" ],
        "B":	[ "Boron",	        10.811,     "p" ],
        "Ba":	[ "Barium",	        137.327,    "s" ],
        "Be":	[ "Beryllium",	    9.012182,   "s" ],
        "Bi":	[ "Bismuth",	    208.9804,   "p" ],
        "Br":	[ "Bromine",	    79.904,     "p" ],
        "C":	[ "Carbon",	        12.0107,    "p" ],
        "Ca":	[ "Calcium",	    40.078,     "s" ],
        "Cd":	[ "Cadmium",	    112.411,    "d" ],
        "Ce":	[ "Cerium",	        140.116,    "f" ],
        "Cl":	[ "Chlorine",	    35.453,     "p" ],
        "Co":	[ "Cobalt",	        58.933195,  "d" ],
        "Cr":	[ "Chromium",	    51.9961,    "d" ],
        "Cs":	[ "Cesium",	        132.9054519,"s" ],
        "Cu":	[ "Copper",	        63.546,     "d" ],
        "Dy":	[ "Dysprosium",	    162.5,      "f" ],
        "Er":	[ "Erbium",	        167.259,    "f" ],
        "Eu":	[ "Europium",	    151.964,    "f" ],
        "F":	[ "Fluorine",	    18.9984032, "p" ],
        "Fe":	[ "Iron",	        55.845,     "d" ],
        "Fr":	[ "Francium",	    223,        "s" ],
        "Ga":	[ "Gallium",	    69.723,     "p" ],
        "Gd":	[ "Gadolinium",	    157.25,     "f" ],
        "Ge":	[ "Germanium",	    72.64,      "p" ],
        "H":	[ "Hydrogen",	    1.00794,    "s" ],
        "He":	[ "Helium",	        4.002602,   "s" ],
        "Hf":	[ "Hafnium",	    178.49,     "d" ],
        "Hg":	[ "Mercury",	    200.59,     "d" ],
        "Ho":	[ "Holmium",	    164.93032,  "f" ],
        "I":	[ "Iodine",	        126.90447,  "p" ],
        "In":	[ "Indium",	        114.818,    "p" ],
        "Ir":	[ "Iridium",	    192.217,    "d" ],
        "K":	[ "Potassium",	    39.0983,    "s" ],
        "Kr":	[ "Krypton",	    83.798,     "p" ],
        "La":	[ "Lanthanum",	    138.90547,  "f" ],
        "Li":	[ "Lithium",	    6.941,      "s" ],
        "Lu":	[ "Lutetium",	    174.9668,   "d" ],
        "Mg":	[ "Magnesium",	    24.305,     "s" ],
        "Mn":	[ "Manganese",	    54.938045,  "d" ],
        "Mo":	[ "Molybdenum",	    95.96,      "d" ],
        "N":	[ "Nitrogen",	    14.0067,    "p" ],
        "Na":	[ "Sodium",	        22.98976928,"s" ],
        "Nb":	[ "Niobium",	    92.90638,   "d" ],
        "Nd":	[ "Neodymium",	    144.242,    "f" ],
        "Ne":	[ "Neon",	        20.1797,    "p" ],
        "Ni":	[ "Nickel",	        58.6934,    "d" ],
        "Np":	[ "Neptunium",	    237,        "f" ],
        "O":	[ "Oxygen",	        15.9994,    "p" ],
        "Os":	[ "Osmium",	        190.23,     "d" ],
        "P":	[ "Phosphorus",	    30.973762,  "p" ],
        "Pa":	[ "Protactinium",	231.03588,  "f" ],
        "Pb":	[ "Lead",	        207.2,      "p" ],
        "Pd":	[ "Palladium",	    106.42,     "d" ],
        "Pm":	[ "Promethium",	    145,        "f" ],
        "Po":	[ "Polonium",	    209,        "p" ],
        "Pr":	[ "Praseodymium",	140.90765,  "f" ],
        "Pt":	[ "Platinum",	    195.084,    "d" ],
        "Pu":	[ "Plutonium",	    244,        "f" ],
        "Ra":	[ "Radium",	        226,        "s" ],
        "Rb":	[ "Rubidium",	    85.4678,    "s" ],
        "Re":	[ "Rhenium",	    186.207,    "d" ],
        "Rh":	[ "Rhodium",	    102.9055,   "d" ],
        "Rn":	[ "Radon",	        222,        "p" ],
        "Ru":	[ "Ruthenium",	    101.07,     "d" ],
        "S":	[ "Sulfur",	        32.065,     "p" ],
        "Sb":	[ "Antimony",	    121.76,     "p" ],
        "Sc":	[ "Scandium",	    44.955912,  "d" ],
        "Se":	[ "Selenium",	    78.96,      "p" ],
        "Si":	[ "Silicon",	    28.0855,    "p" ],
        "Sm":	[ "Samarium",	    150.36,     "f" ],
        "Sn":	[ "Tin",	        118.71,     "p" ],
        "Sr":	[ "Strontium",	    87.62,      "s" ],
        "Ta":	[ "Tantalum",	    180.94788,  "d" ],
        "Tb":	[ "Terbium",	    158.92535,  "f" ],
        "Tc":	[ "Technetium",	    98,         "d" ],
        "Te":	[ "Tellurium",	    127.6,      "p" ],
        "Th":	[ "Thorium",	    232.03806,  "f" ],
        "Ti":	[ "Titanium",	    47.867,     "d" ],
        "Tl":	[ "Thallium",	    204.3833,   "p" ],
        "Tm":	[ "Thulium",	    168.93421,  "f" ],
        "U":	[ "Uranium",	    238.02891,  "f" ],
        "V":	[ "Vanadium",	    50.9415,    "d" ],
        "W":	[ "Tungsten",	    183.84,     "d" ],
        "Xe":	[ "Xenon",	        131.293,    "p" ],
        "Y":	[ "Yttrium",	    88.90585,   "d" ],
        "Yb":	[ "Ytterbium",	    173.054,    "f" ],
        "Zn":	["Zinc",	        65.38,      "d"],
        "Zr": 	["Zirconium",	    91.224,     "d"],
    }
    return table

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    '''
    FOR:    computing the total elemental mass of a chemical symbol 
    PARAM:  list containing the element symbols and quantity of that element, amd the dict containing the periodic table
    RETURN: total molar mass as a float
    '''
    CHEM_SYMBOL_POS = 0
    CHEM_QUANTITY_POS = 1
    PERIODIC_TABLE_MASS_POS = 1

    total_molar_mass = 0.0

    for item in symbol_quantity_list:
        symbol_element_mass = periodic_table_dict[item[CHEM_SYMBOL_POS]][PERIODIC_TABLE_MASS_POS]
        total_molar_mass += symbol_element_mass * item[CHEM_QUANTITY_POS]

    return total_molar_mass

def get_sample_element_blocks(symbol_list, periodic_table_dict):
    '''
    FOR:    creating a list containing the qunatity of distinct elements from each block
    PARAM:  list containing the element symbols and quantity of that element, amd the dict containing the periodic table
    RETURN: Dict of element blocks and how many distinct elements are represented from said block.
    '''
    
    CHEM_SYMBOL_POS = 0
    CHEM_BLOCK_POS = 1
    PERIODIC_TABLE_BLOCK_POS = 2

    block_list = {}
    for element in symbol_list:
        element_block = periodic_table_dict[element[CHEM_SYMBOL_POS]][PERIODIC_TABLE_BLOCK_POS]
        if  element_block in block_list:
            block_list[element_block] += 1
        else:
            block_list[element_block] = 1

    return block_list


# Main call
if __name__ == "__main__":
    main()