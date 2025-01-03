import numpy as np
import math as m
import pandas as pd

def parse_atoms(lines):
    """
    Parses the atom data from the lines and returns the Cd and Se atom lists.

    Args:
        lines (list): A list of strings, each representing a line in the input file.

    Returns:
        tuple: Two lists, one for Cd atoms and one for Se atoms.
    """
    Cd = []
    Se = []
    j = 0
    k = 0
    for i, line in enumerate(lines):
        str1 = line.split()
        if str1[0] == 'O':
            Se.append([i + 1, float(str1[1]), float(str1[2]), float(str1[3])])
            j += 1
        elif str1[0] == 'Zn':
            Cd.append([i + 1, float(str1[1]), float(str1[2]), float(str1[3])])
            k += 1
    return Cd, Se