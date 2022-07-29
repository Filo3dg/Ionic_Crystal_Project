import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    # create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #    if conn:
    #        conn.close()
    return conn


if __name__ == '__main__':
    conn = create_connection('Basis_Set.db')


cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pobtzvprev2(
                  n_atom integer,
                  elem text,
                  b_set text
                  )""")

periodic_table = [{'n_atom': 1, 'elem': 'H', 'b_set': 'pobtzvprev2/H.txt'},
                  {'n_atom': 3, 'elem': 'Li', 'b_set': 'pobtzvprev2/Li.txt'},
                  {'n_atom': 4, 'elem': 'Be', 'b_set': 'pobtzvprev2/Be.txt'},
                  {'n_atom': 5, 'elem': 'B', 'b_set': 'pobtzvprev2/B.txt'},
                  {'n_atom': 6, 'elem': 'C', 'b_set': 'pobtzvprev2/C.txt'},
                  {'n_atom': 7, 'elem': 'N', 'b_set': 'pobtzvprev2/N.txt'},
                  {'n_atom': 8, 'elem': 'O', 'b_set': 'pobtzvprev2/O.txt'},
                  {'n_atom': 9, 'elem': 'F', 'b_set': 'pobtzvprev2/F.txt'},
                  {'n_atom': 11, 'elem': 'Na', 'b_set': 'pobtzvprev2/Na.txt'},
                  {'n_atom': 12, 'elem': 'Mg', 'b_set': 'pobtzvprev2/Mg.txt'},
                  {'n_atom': 13, 'elem': 'Al', 'b_set': 'pobtzvprev2/Al.txt'},
                  {'n_atom': 14, 'elem': 'Si', 'b_set': 'pobtzvprev2/Si.txt'},
                  {'n_atom': 15, 'elem': 'P', 'b_set': 'pobtzvprev2/P.txt'},
                  {'n_atom': 16, 'elem': 'S', 'b_set': 'pobtzvprev2/S.txt'},
                  {'n_atom': 17, 'elem': 'Cl', 'b_set': 'pobtzvprev2/Cl.txt'},
                  {'n_atom': 19, 'elem': 'K', 'b_set': 'pobtzvprev2/K.txt'},
                  {'n_atom': 20, 'elem': 'Ca', 'b_set': 'pobtzvprev2/Ca.txt'},
                  {'n_atom': 21, 'elem': 'Sc', 'b_set': 'pobtzvprev2/Sc.txt'},
                  {'n_atom': 22, 'elem': 'Ti', 'b_set': 'pobtzvprev2/Ti.txt'},
                  {'n_atom': 23, 'elem': 'V', 'b_set': 'pobtzvprev2/V.txt'},
                  {'n_atom': 24, 'elem': 'Cr', 'b_set': 'pobtzvprev2/Cr.txt'},
                  {'n_atom': 25, 'elem': 'Mn', 'b_set': 'pobtzvprev2/Mn.txt'},
                  {'n_atom': 26, 'elem': 'Fe', 'b_set': 'pobtzvprev2/Fe.txt'},
                  {'n_atom': 27, 'elem': 'Co', 'b_set': 'pobtzvprev2/Co.txt'},
                  {'n_atom': 28, 'elem': 'Ni', 'b_set': 'pobtzvprev2/Ni.txt'},
                  {'n_atom': 29, 'elem': 'Cu', 'b_set': 'pobtzvprev2/Cu.txt'},
                  {'n_atom': 30, 'elem': 'Zn', 'b_set': 'pobtzvprev2/Zn.txt'},
                  {'n_atom': 31, 'elem': 'Ga', 'b_set': 'pobtzvprev2/Ga.txt'},
                  {'n_atom': 32, 'elem': 'Ge', 'b_set': 'pobtzvprev2/Ge.txt'},
                  {'n_atom': 33, 'elem': 'As', 'b_set': 'pobtzvprev2/As.txt'},
                  {'n_atom': 34, 'elem': 'Se', 'b_set': 'pobtzvprev2/Se.txt'},
                  {'n_atom': 35, 'elem': 'Br', 'b_set': 'pobtzvprev2/Br.txt'},
                  {'n_atom': 37, 'elem': 'Rb', 'b_set': 'pobtzvprev2/Rb.txt'},
                  {'n_atom': 38, 'elem': 'Sr', 'b_set': 'pobtzvprev2/Sr.txt'},
                  {'n_atom': 39, 'elem': 'Y', 'b_set': 'pobtzvprev2/Y.txt'},
                  {'n_atom': 40, 'elem': 'Zr', 'b_set': 'pobtzvprev2/Zr.txt'},
                  {'n_atom': 41, 'elem': 'Nb', 'b_set': 'pobtzvprev2/Nb.txt'},
                  {'n_atom': 42, 'elem': 'Mo', 'b_set': 'pobtzvprev2/Mo.txt'},
                  {'n_atom': 44, 'elem': 'Ru', 'b_set': 'pobtzvprev2/Ru.txt'},
                  {'n_atom': 45, 'elem': 'Rh', 'b_set': 'pobtzvprev2/Rh.txt'},
                  {'n_atom': 46, 'elem': 'Pd', 'b_set': 'pobtzvprev2/Pd.txt'},
                  {'n_atom': 47, 'elem': 'Ag', 'b_set': 'pobtzvprev2/Ag.txt'},
                  {'n_atom': 48, 'elem': 'Cd', 'b_set': 'pobtzvprev2/Cd.txt'},
                  {'n_atom': 49, 'elem': 'In', 'b_set': 'pobtzvprev2/In.txt'},
                  {'n_atom': 50, 'elem': 'Sn', 'b_set': 'pobtzvprev2/Sn.txt'},
                  {'n_atom': 51, 'elem': 'Sb', 'b_set': 'pobtzvprev2/Sb.txt'},
                  {'n_atom': 52, 'elem': 'Te', 'b_set': 'pobtzvprev2/Te.txt'},
                  {'n_atom': 53, 'elem': 'I', 'b_set': 'pobtzvprev2/I.txt'},
                  {'n_atom': 55, 'elem': 'Cs', 'b_set': 'pobtzvprev2/Cs.txt'},
                  {'n_atom': 56, 'elem': 'Ba', 'b_set': 'pobtzvprev2/Ba.txt'},
                  {'n_atom': 72, 'elem': 'Hf', 'b_set': 'pobtzvprev2/Hf.txt'},
                  {'n_atom': 73, 'elem': 'Ta', 'b_set': 'pobtzvprev2/Ta.txt'},
                  {'n_atom': 74, 'elem': 'W', 'b_set': 'pobtzvprev2/W.txt'},
                  {'n_atom': 75, 'elem': 'Re', 'b_set': 'pobtzvprev2/Re.txt'},
                  {'n_atom': 76, 'elem': 'Os', 'b_set': 'pobtzvprev2/Os.txt'},
                  {'n_atom': 77, 'elem': 'Ir', 'b_set': 'pobtzvprev2/Ir.txt'},
                  {'n_atom': 78, 'elem': 'Pt', 'b_set': 'pobtzvprev2/Pt.txt'},
                  {'n_atom': 79, 'elem': 'Au', 'b_set': 'pobtzvprev2/Au.txt'},
                  {'n_atom': 80, 'elem': 'Hg', 'b_set': 'pobtzvprev2/Hg.txt'},
                  {'n_atom': 81, 'elem': 'Tl', 'b_set': 'pobtzvprev2/Tl.txt'},
                  {'n_atom': 82, 'elem': 'Pb', 'b_set': 'pobtzvprev2/Pb.txt'},
                  {'n_atom': 83, 'elem': 'Bi', 'b_set': 'pobtzvprev2/Bi.txt'},
                  {'n_atom': 84, 'elem': 'Po', 'b_set': 'pobtzvprev2/Po.txt'}
                  ]

for elements in periodic_table:
    basis_set = str()
    bset = elements.get('b_set')
    bset = open(bset)
    lines = bset.readlines()
    for function in lines:
        basis_set = basis_set+function
    elements.update({'b_set': basis_set})

# cursor.executemany()

conn.commit()

conn.close()
