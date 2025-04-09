import json
import sqlite3
import numpy as np
import pandas as pd

from itertools import product
from math import isnan
from tqdm import tqdm

con = sqlite3.connect('db.db')
cur = con.cursor()

day_to_int = {
    'MON': 1,
    'TUE': 2,
    'WED': 3,
    'THU': 4,
    'FRI': 5
}

mods = ['SC1007', 'SC2002', 'SC2006', 'MH2100', 'MH2802']
# mods = ['SC1007', 'SC2002', 'SC2006', 'MH2100', 'MH2500']

course_indices = {mod: sorted({i[0] for i in cur.execute('SELECT tutorial_index FROM NTU WHERE course_code=?', [mod]).fetchall()}) for mod in mods}

possible_timetables = []

permutations = 1
for i in course_indices.values():
    permutations *= len(i)

print(permutations)

default = pd.DataFrame(columns=range(1, 6), index=range(8, 24))
for mod in mods:
    for day, start_time, end_time in cur.execute('SELECT day, start_time, end_time FROM NTU WHERE course_code = ? AND tutorial_index = \'0\'', [mod]).fetchall():
        for hour in range(int(start_time[:2]), int(end_time[:2])):
            if type(default[day_to_int[day]][hour]) == str:
                print('Not possible')
                exit()
            else:
                default.loc[hour, day_to_int[day]] = mod

clashes = []

for combination in tqdm(product(*list(course_indices.values()))):
    if '0' in combination:
        continue
    
    timetable = default.copy(deep=True)
    clash = False
    for pair in product(combination, repeat=2):
        if set(map(int, pair)) in clashes:
            clash = True
            break
    
    if clash:
        continue

    for mod, tutorial_index in zip(mods, combination):
        for day, start_time, end_time in cur.execute('SELECT day, start_time, end_time FROM NTU WHERE course_code = ? AND tutorial_index = ?', [mod, tutorial_index]).fetchall():
            for hour in range(int(start_time[:2]), int(end_time[:2])):
                if type(timetable[day_to_int[day]][hour]) == str:
                    clash = True
                elif isnan(timetable[day_to_int[day]][hour]):
                    timetable.loc[hour, day_to_int[day]] = int(tutorial_index)
                else:
                    clashes.append({int(tutorial_index), timetable[day_to_int[day]][hour]})
                    clash = True
    
    if not clash:
        possible_timetables.append(timetable)

best_free_days = -1
best_start_times = 0
best_timetable = None

for timetable in possible_timetables:
    free_days = sum([timetable[i].isna().all() for i in range(1, 6)])
    start_times = []
    for i in range(1, 6):
        try:
            start_times.append(timetable.index[timetable[i].notna()][0])
        except Exception as e:
            pass
    
    start_times = sum(start_times)
    
    if free_days > best_free_days or (free_days == best_free_days and start_times > best_start_times):
        best_free_days = free_days
        best_start_times = start_times
        best_timetable = timetable

best_timetable.to_csv('timetable.csv')