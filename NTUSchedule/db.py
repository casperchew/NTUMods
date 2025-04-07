import re
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

try:
    cur.execute('DROP TABLE NTU')
except Exception as e:
    pass

cur.execute('''CREATE TABLE NTU(
    course_code,
    tutorial_index,
    type,
    day,
    time
)''')

html = open('courses.html', 'r').read()

for mod in re.findall(r'<table >[\w\W]*?</table>\n<table  border>[\w\W]*?</table>', html):
    course_info, course_schedule = re.findall(r'<table[\w\W]*?</table>', mod)
    course_code = re.findall(r'<TD WIDTH="100"><B><FONT COLOR=#0000FF>([\w\W]*?)</FONT></B></TD>', course_info)[0]

    classes = re.findall(r'<TR[\w\W]*?</tr>', course_schedule)
    for i in classes:
        data = re.findall(r'<td><b>([\w\W]*?)</b></td>', i)
        try:
            cur.execute(f'INSERT INTO NTU VALUES (?, ?, ?, ?, ?)', [course_code, data[0], data[1], data[3], data[4]])
            con.commit()
        except Exception as e:
            pass