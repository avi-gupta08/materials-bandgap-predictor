import numpy as np
import matplotlib.pyplot as plt

# 1. Periodic Table Lookup Dictionary
# Format: 'Element': [Pauling Electronegativity, Atomic Radius (Angstroms), Valence Electrons]
PERIODIC_TABLE = {
    "H":  [2.20, 0.53, 1], "Li": [0.98, 1.67, 1], "Be": [1.57, 1.12, 2],
    "B":  [2.04, 0.87, 3], "C":  [2.55, 0.67, 4], "N":  [3.04, 0.56, 5],
    "O":  [3.44, 0.48, 6], "F":  [3.98, 0.42, 7], "Na": [0.93, 1.90, 1],
    "Mg": [1.31, 1.45, 2], "Al": [1.61, 1.18, 3], "Si": [1.90, 1.11, 4],
    "P":  [2.19, 0.98, 5], "S":  [2.58, 0.88, 6], "Cl": [3.16, 0.79, 7],
    "K":  [0.82, 2.43, 1], "Ca": [1.00, 1.94, 2], "Ti": [1.54, 1.76, 4],
    "Zn": [1.65, 1.42, 2], "Ga": [1.81, 1.36, 3], "Ge": [2.01, 1.25, 4],
    "As": [2.18, 1.14, 5], "Se": [2.55, 1.03, 6], "Br": [2.96, 0.94, 7],
    "Sr": [0.95, 2.19, 2], "Cd": [1.69, 1.61, 2], "In": [1.78, 1.56, 3],
    "Sn": [1.96, 1.45, 4], "Sb": [2.05, 1.33, 5], "Te": [2.10, 1.23, 6],
    "Ba": [0.89, 2.53, 2],
}

# 2. Real Semiconductor Dataset: (Formula_Dict, Real_Bandgap_in_eV)
MATERIALS_DATA = [
    ({"Si": 1}, 1.12),           ({"Ge": 1}, 0.66),           ({"C": 1}, 5.47),
    ({"Ga": 1, "As": 1}, 1.42),  ({"Ga": 1, "N": 1}, 3.40),   ({"Ga": 1, "P": 1}, 2.26),
    ({"In": 1, "P": 1}, 1.34),   ({"In": 1, "As": 1}, 0.35),  ({"In": 1, "N": 1}, 0.70),
    ({"Al": 1, "N": 1}, 6.20),   ({"Al": 1, "P": 1}, 2.45),   ({"Al": 1, "As": 1}, 2.16),
    ({"Zn": 1, "O": 1}, 3.37),   ({"Zn": 1, "S": 1}, 3.54),   ({"Zn": 1, "Se": 1}, 2.70),
    ({"Zn": 1, "Te": 1}, 2.26),  ({"Cd": 1, "S": 1}, 2.42),   ({"Cd": 1, "Se": 1}, 1.74),
    ({"Cd": 1, "Te": 1}, 1.49),  ({"Ti": 1, "O": 2}, 3.20),   ({"Sn": 1, "O": 2}, 3.60),
    ({"Mg": 1, "O": 1}, 7.80),   ({"Ca": 1, "O": 1}, 7.00),   ({"Sr": 1, "Ti": 1, "O": 3}, 3.25),
    ({"Ba": 1, "Ti": 1, "O": 3}, 3.20), ({"Si": 1, "C": 1}, 3.26), ({"B": 1, "N": 1}, 5.96),
    ({"Ga": 2, "O": 3}, 4.80),   ({"Al": 2, "O": 3}, 8.80),   ({"Si": 1, "O": 2}, 8.90),
]

# --- YOUR CODE FOR TASK 1 GOES BELOW ---
def extract_features(comp):
    # comp is a dictionary like {"Ti": 1, "O": 2}
    # Write a loop to calculate:
    # 1. en_diff (max electronegativity - min electronegativity)
    # 2. avg_en (weighted average electronegativity)
    # 3. avg_radius (weighted average atomic radius)
    pass

# Test it on TiO2 once you write it:
print("Testing TiO2:", extract_features({"Ti": 1, "O": 2}))

print("hello")