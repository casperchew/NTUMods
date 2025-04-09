import sqlite3

import pandas as pd

from math import isnan

con = sqlite3.connect('db.db')
cur = con.cursor()

timetable = pd.read_csv('timetable.csv', index_col=0)

def index_lookup(tutorial_index):
    try:
        tutorial_index = int(tutorial_index)
    except Exception as e:
        if type(tutorial_index) == str:
            return f'{tutorial_index} LEC'
        else:
            return tutorial_index

    if not isnan(tutorial_index):
        query = cur.execute('SELECT course_code FROM NTU WHERE tutorial_index = ?', [str(int(tutorial_index))]).fetchone()
        if query:
            return f'{query[0]} {tutorial_index}'
    
    return tutorial_index

timetable = timetable.map(index_lookup)

print(timetable)