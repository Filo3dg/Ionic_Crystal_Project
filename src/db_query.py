import sqlite3 as sl
from sqlite3 import Error
import os


def get_bset(element: str):

    # Dictionary for the periodic table
    periodic_table = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
                      'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
                      'K': 19, 'Ca': 20, 'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27,
                      'Ni': 28, 'Cu': 29, 'Zn': 30, 'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36,
                      'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40, 'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45,
                      'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54,
                      'Cs': 55, 'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60, 'Pm': 61, 'Sm': 62, 'Eu': 63,
                      'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70, 'Lu': 71, 'Hf': 72,
                      'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80, 'Tl': 81,
                      'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86, 'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90,
                      'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99,
                      'Fm': 100, 'Md': 101, 'No': 102, 'Lr': 103}

    db_file = os.path.join('database', 'Basis_Set.db')

    # create a database connection to a SQLite database
    conn = None
    try:
        conn = sl.connect(db_file)
        print(sl.version)
    except Error as e:
        print(e)

    # cursor creation for the database creation
    cursor = conn.cursor()

    # gets the atomic number for the element selected
    n_atom = periodic_table[element]

    # gets the basis set from the database
    cursor.execute("""SELECT b_set FROM pobtzvprev2 WHERE n_atom=? AND elem=?""", [
                   n_atom, element])

    basis_set = cursor.fetchall()

    return basis_set


def connect_db(db_file):

    import sqlite3 as sl
    from sqlite3 import Error

    conn = None

    try:
        conn = sl.connect(db_file)
    except Error as e:
        print(e)

    return conn
