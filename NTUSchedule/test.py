import sqlite3

from pprint import pprint

con = sqlite3.connect('db.db')
cur = con.cursor()

# query = cur.execute('SELECT * FROM NTU WHERE tutorial_index = \'82201\'')
query = cur.execute('SELECT * FROM NTU WHERE course_code = ? AND tutorial_index = \'10197\'', ['SC2006'])
pprint(query.fetchall())