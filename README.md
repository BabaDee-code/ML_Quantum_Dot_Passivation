This repository contains code for calculating the bonds between Cd (Cadmium) and Se (Selenium) atoms in a quantum dot structure, assigning hydrogen coordinates, and writing the results to an output file. The project is structured into multiple Python modules for better modularity and maintainability.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
  - [file_io.py](#file_iopy)
  - [atom_parser.py](#atom_parserpy)
  - [bond_calculator.py](#bond_calculatorpy)
  - [h_coordinates.py](#h_coordinatespy)
  - [main.py](#mainpy)
- [Input File Format](#input-file-format)
- [Output File Format](#output-file-format)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   \`\`\`sh
   git clone https://github.com/BabaDee-code/ML_Quantum_Dot_Passivation.git
   cd ML_Quantum_Dot_Passivation
   \`\`\`

2. (Optional) Create and activate a virtual environment:
   \`\`\`sh
   python -m venv venv
   source venv/bin/activate  # On Windows use \`venv\Scripts\activate\`
   \`\`\`

3. Install the required dependencies:
   \`\`\`sh
   pip install -r requirements.txt
   \`\`\`

## Usage

1. Prepare the input file \`INPUT2.txt\` with the atom data.
2. Run the main script:
   \`\`\`sh
   python main.py
   \`\`\`
3. The output will be saved in \`HBonds.txt\`.

## Project Structure

\`\`\`
ML_Quantum_Dot_Passivation/
├── atom_parser.py
├── bond_calculator.py
├── file_io.py
├── h_coordinates.py
├── main.py
├── INPUT2.txt
├── HBonds.txt
└── README.md
\`\`\`

## Modules

### file_io.py

This module contains functions for reading and writing files.

- \`read_input_file(filename)\`: Reads the input file and returns the lines.
- \`write_output_file(filename, H)\`: Writes the hydrogen coordinates to the output file.

### atom_parser.py

This module contains functions for parsing atom data.

- \`parse_atoms(lines)\`: Parses the atom data from the lines and returns the Cd and Se atom lists.

### bond_calculator.py

This module contains functions for calculating bonds between Cd and Se atoms.

- \`calculate_bonds(Cd, Se, bondLength)\`: Calculates the bonds between Cd and Se atoms.

### h_coordinates.py

This module contains functions for assigning hydrogen coordinates to the atoms.

- \`assign_h_coordinates(Cd, Se, Cd_bond, Se_bond, bondLength, sEH, cDH, noSeAtoms)\`: Assigns the hydrogen coordinates for the atoms.

### main.py

This is the main script that orchestrates the reading of the input file, parsing atoms, calculating bonds, assigning hydrogen coordinates, and writing the output file.

## Input File Format

The input file \`INPUT2.txt\` should contain the atom data with each line representing an atom in the following format:

\`\`\`
<atom_type> <x_coordinate> <y_coordinate> <z_coordinate>
\`\`\`

Example:
\`\`\`
O 1.234 2.345 3.456
Zn 4.567 5.678 6.789
\`\`\`

## Output File Format

The output file \`HBonds.txt\` will contain the calculated hydrogen bond coordinates for the atoms in the following format:

\`\`\`
H      <x_coordinate>     <y_coordinate>     <z_coordinate>
\`\`\`

Example:
\`\`\`
H      1.23400000     2.34500000     3.45600000
H1     4.56700000     5.67800000     6.78900000
\`\`\`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details." > README.md

# Add the README.md file to the staging area
git add README.md

# Commit the changes
git commit -m "Add detailed README.md"

# Push the changes to the remote repository
git push origin main