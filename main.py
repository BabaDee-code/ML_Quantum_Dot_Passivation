from file_io import read_input_file, write_output_file
from atom_parser import parse_atoms
from bond_calculator import calculate_bonds
from h_coordinates import assign_h_coordinates

def main():
    """
    Main function to read input file, parse atoms, calculate bonds, assign hydrogen coordinates, and write output file.
    """
    input_filename = "INPUT2.txt"
    output_filename = "HBonds.txt"
    bondLength = 2.01242
    noSeAtoms = 1015
    sEH = 0.515385
    cDH = 0.511538

    lines = read_input_file(input_filename)
    Cd, Se = parse_atoms(lines)
    Cd_bond, Se_bond = calculate_bonds(Cd, Se, bondLength)
    H = assign_h_coordinates(Cd, Se, Cd_bond, Se_bond, bondLength, sEH, cDH, noSeAtoms)
    write_output_file(output_filename, H)

if __name__ == "__main__":
    main()
