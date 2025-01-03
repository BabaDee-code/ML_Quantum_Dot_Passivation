import math as m
import numpy as np
import pandas as pd

def calculate_bonds(Cd, Se, bondLength):
    """
    Calculates the bonds between Cd and Se atoms.

    Args:
        Cd (list): A list of Cd atoms.
        Se (list): A list of Se atoms.
        bondLength (float): The bond length threshold.

    Returns:
        tuple: Two lists, one for Cd bonds and one for Se bonds.
    """
    Cd_bond = []
    Se_bond = []
    for i in range(len(Se)):
        Se_bond.append([Se[i][0]])
        for l in range(len(Cd)):
            d = m.sqrt((Se[i][1] - Cd[l][1])**2 + (Se[i][2] - Cd[l][2])**2 + (Se[i][3] - Cd[l][3])**2)
            if d < bondLength + 0.5:
                Se_bond[i].append(Cd[l][0])
    for i in range(len(Cd)):
        Cd_bond.append([Cd[i][0]])
        for l in range(len(Se)):
            d = m.sqrt((Cd[i][1] - Se[l][1])**2 + (Cd[i][2] - Se[l][2])**2 + (Cd[i][3] - Se[l][3])**2)
            if d < bondLength + 0.5:
                Cd_bond[i].append(Se[l][0])
    return Cd_bond, Se_bond