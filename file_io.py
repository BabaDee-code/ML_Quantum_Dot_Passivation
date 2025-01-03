import numpy as np
import math as m
import pandas as pd

def read_input_file(filename):
    """
    Reads the input file and returns the lines.

    Args:
        filename (str): The name of the input file.

    Returns:
        list: A list of strings, each representing a line in the file.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def write_output_file(filename, H):
    """
    Writes the hydrogen coordinates to the output file.

    Args:
        filename (str): The name of the output file.
        H (list): A list of hydrogen coordinates.
    """
    with open(filename, 'w') as file:
        for i in range(len(H)):
            x = H[i][1]
            y = H[i][2]
            z = H[i][3]
            s = "H      " if i < len(H) / 2 else "H1      "
            s += f"{x:9.8f}     {y:9.8f}     {z:9.8f}\n"
            file.write(s)