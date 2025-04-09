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
    start_time,
    end_time,
    remark
)''')

html = open('courses.html', 'r').read()

previous_index = None

for mod in re.findall(r'<table >[\w\W]*?</table>\n<table  border>[\w\W]*?</table>', html):
    course_info, course_schedule = re.findall(r'<table[\w\W]*?</table>', mod)
    course_code = re.findall(r'<TD WIDTH="100"><B><FONT COLOR=#0000FF>([\w\W]*?)</FONT></B></TD>', course_info)[0]

    classes = re.findall(r'<TR[\w\W]*?</tr>', course_schedule)
    for i in classes:
        data = re.findall(r'<td><b>([\w\W]*?)</b></td>', i)
        if data[0]:
            previous_index = data[0]

        try:
            time = data[4].split('-')
            if not cur.execute('SELECT * FROM NTU WHERE course_code = ? AND type = ? AND day = ? AND start_time = ? AND remark = ?', [course_code, data[1], data[3], time[0], data[6]]).fetchall():
                # if course_code == 'MH1805':
                #     print(cur.execute('SELECT * FROM NTU WHERE course_code = ? AND day = ? AND start_time = ?', [course_code, data[3], time[0]]).fetchall())
                # break
                cur.execute(f'INSERT INTO NTU VALUES (?, ?, ?, ?, ?, ?, ?)', [course_code, previous_index, data[1], data[3], time[0], time[1], data[6]])
        except Exception as e:
            pass

cur.execute('UPDATE NTU SET tutorial_index = \'0\' WHERE type = ?', ['LEC/STUDIO'])

con.commit()