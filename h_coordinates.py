import numpy as np
import math as m
import pandas as pd


def assign_h_coordinates(Cd, Se, Cd_bond, Se_bond, bondLength, sEH, cDH, noSeAtoms):
    """
    Assigns the hydrogen coordinates for the atoms.

    Args:
        Cd (list): A list of Cd atoms.
        Se (list): A list of Se atoms.
        Cd_bond (list): A list of Cd bonds.
        Se_bond (list): A list of Se bonds.
        bondLength (float): The bond length threshold.
        sEH (float): The sEH parameter.
        cDH (float): The cDH parameter.
        noSeAtoms (int): The number of Se atoms.

    Returns:
        list: A list of hydrogen coordinates.
    """
    H = []
    n = 0
    for i in range(len(Se)):
        cnt = len(Se_bond[i])
        z_atom = 0
        y_atom = 0
        y_atom_cnt = 0
        if cnt < 5:
            for m1 in range(1, len(Se_bond[i])):
                if abs(Cd[Se_bond[i][m1] - noSeAtoms][1] - Se[i][1]) < 0.05 and abs(Cd[Se_bond[i][m1] - noSeAtoms][2] - Se[i][2]) < 0.05:
                    z_atom = 1
            if z_atom != 1:
                H.append([i + 1, Se[i][1], Se[i][2], Se[i][3] - bondLength * sEH])
                n += 1
            for m1 in range(1, len(Se_bond[i])):
                if abs(Cd[Se_bond[i][m1] - noSeAtoms][1] - Se[i][1]) < 0.2 and abs(Cd[Se_bond[i][m1] - noSeAtoms][2]) > 0.05 and abs(Cd[Se_bond[i][m1] - noSeAtoms][3]) > 0.05:
                    z_atom = 2
                    y_no1 = Se_bond[i][m1] - noSeAtoms
                elif abs(Cd[Se_bond[i][m1] - noSeAtoms][1] - Se[i][1]) > 0.05 and abs(Cd[Se_bond[i][m1] - noSeAtoms][2]) > 0.05:
                    y_atom_cnt += 1
                    y_no = Se_bond[i][m1] - noSeAtoms
                    if Cd[Se_bond[i][m1] - noSeAtoms][2] - Se[i][2] > 0:
                        y_atom = 1
                    else:
                        y_atom = 2
            if z_atom != 2:
                H.append([i + 1, Se[i][1], Se[i][2] - (bondLength * 0.94305793) * sEH if y_atom == 1 else Se[i][2] + (bondLength * 0.94305793) * sEH, Se[i][3] + (bondLength * 0.333333) * sEH])
                n += 1
            if y_atom_cnt < 2:
                H.append([i + 1, Se[i][1] + (bondLength * 0.81671415) * sEH if y_atom_cnt == 1 and Cd[y_no][1] - Se[i][1] < 0 else Se[i][1] - (bondLength * 0.81671415) * sEH, Cd[y_no][2] - (bondLength * 0.471532764) * (1 - sEH) if Cd[y_no][2] - Se[i][2] > 0 else Cd[y_no][2] + (bondLength * 0.471532764) * (1 - sEH), Se[i][3] + (bondLength * 0.333333) * sEH])
                n += 1
                if y_atom_cnt == 0:
                    H.append([i + 1, Se[i][1] - (bondLength * 0.81671415) * sEH, Se[i][2] + (bondLength * 0.471532764) * sEH if Cd[y_no1][2] - Se[i][2] < 0 else Se[i][2] - (bondLength * 0.471532764) * sEH, Se[i][3] + (bondLength * 0.333333) * sEH])
                    n += 1
                    H.append([i + 1, Se[i][1] + (bondLength * 0.81671415) * sEH, H[n - 1][2], Se[i][3] + (bondLength * 0.333333) * sEH])
                    n += 1
    for i in range(len(Cd)):
        cnt = len(Cd_bond[i])
        z_atom = 0
        y_atom = 0
        y_atom_cnt = 0
        if cnt < 5:
            for m1 in range(1, len(Cd_bond[i])):
                if abs(Se[Cd_bond[i][m1] - noSeAtoms][1] - Cd[i][1]) < 0.05 and abs(Se[Cd_bond[i][m1] - noSeAtoms][2] - Cd[i][2]) < 0.05:
                    z_atom = 1
            if z_atom != 1:
                H.append([i + 1, Cd[i][1], Cd[i][2], Cd[i][3] + bondLength * cDH])
                n += 1
            for m1 in range(1, len(Cd_bond[i])):
                if abs(Se[Cd_bond[i][m1] - noSeAtoms][1] - Cd[i][1]) < 0.2 and abs(Se[Cd_bond[i][m1] - noSeAtoms][2]) > 0.05 and abs(Se[Cd_bond[i][m1] - noSeAtoms][3]) > 0.05:
                    z_atom = 2
                    y_no1 = Cd_bond[i][m1] - noSeAtoms
                elif abs(Se[Cd_bond[i][m1] - noSeAtoms][1] - Cd[i][1]) > 0.05 and abs(Se[Cd_bond[i][m1] - noSeAtoms][2]) > 0.05:
                    y_atom_cnt += 1
                    y_no = Cd_bond[i][m1] - noSeAtoms
                    if Se[Cd_bond[i][m1] - noSeAtoms][2] - Cd[i][2] > 0:
                        y_atom = 1
                    else:
                        y_atom = 2
            if z_atom != 2:
                H.append([i + 1, Cd[i][1], Cd[i][2] - (bondLength * 0.94305793) * cDH if y_atom == 1 else Cd[i][2] + (bondLength * 0.94305793) * cDH, Cd[i][3] - (bondLength * 0.333333) * cDH])
                n += 1
            if y_atom_cnt < 2:
                H.append([i + 1, Cd[i][1] + (bondLength * 0.81671415) * cDH if y_atom_cnt == 1 and Se[y_no][1] - Cd[i][1] < 0 else Cd[i][1] - (bondLength * 0.81671415) * cDH, Se[y_no][2] - (bondLength * 0.471532764) * (1 - cDH) if Se[y_no][2] - Cd[i][2] > 0 else Se[y_no][2] + (bondLength * 0.471532764) * (1 - cDH), Cd[i][3] - (bondLength * 0.333333) * cDH])
                n += 1
                if y_atom_cnt == 0:
                    H.append([i + 1, Cd[i][1] - 2.15 * cDH, Cd[i][2] + (bondLength * 0.471532764) * cDH if Se[y_no1][2] - Cd[i][2] < 0 else Cd[i][2] - (bondLength * 0.471532764) * cDH, Cd[i][3] - (bondLength * 0.333333) * cDH])
                    n += 1
                    H.append([i + 1, Cd[i][1] + (bondLength * 0.81671415) * cDH, H[n - 1][2], Cd[i][3] - (bondLength * 0.333333) * cDH])
                    n += 1
    return H