import requests

r = requests.post(
    'https://wish.wis.ntu.edu.sg/webexe/owa/AUS_SCHEDULE.main_display1',
    data={
        'acadsem': '2025;1',
        'r_course_yr': '',
        'r_subj_code': '',
        'r_search_type': 'F',
        'boption': 'Search',
        'staff_access': 'false'
    }
)

with open('courses.html', 'w') as f:
    f.write(r.text)