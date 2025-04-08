import sqlite3

from itertools import product

from pprint import pprint

con = sqlite3.connect('db.db')
cur = con.cursor()

timetable = {i: 0 for i in range(6)}

mods = ['CC0003', 'CC0005', 'SC1007', 'SC2002', 'SC2006', 'MH2100']
course_indices = {i: {i[0] for i in cur.execute('SELECT tutorial_index FROM NTU WHERE course_code = ?', [i]).fetchall()} for i in mods}

for timetable in product(*course_indices.values()):
    pass