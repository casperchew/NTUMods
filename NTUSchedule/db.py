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
    tutorial_group,
    day,
    start_time,
    end_time,
    venue,
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
        print(data)
        if data[0]:
            previous_index = data[0]

        try:
            time = data[4].split('-')
            cur.execute(f'INSERT INTO NTU VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', [course_code, previous_index, data[1], data[2], data[3], time[0], time[1], data[5], data[6]])
        except Exception as e:
            print(e)
            pass
    
con.commit()