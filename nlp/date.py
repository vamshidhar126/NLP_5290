import re
def isValidDate(date):
    date_1 = r'^(January|February|March|April|May|June|July|August|September|October|November|December) (0?[1-9]|[12][0-9]|3[01]), \d{4}$'
    p1 = re.compile(date_1)
    match = p1.finditer(str(date))
    for x in match:
        print('Date found : ',x)
    date_2 = r'^(0?[1-9]|1[0-2])\/(0?[1-9]|[12][0-9]|3[01])\/\d{2}$'
    p2 = re.compile(date_2)
    match = p2.finditer(str(date))
    for x in match:
        print('Date found : ',x)
    date_3 = r'^(0?[1-9]|[12][0-9]|3[01])-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec), \d{4}$'
    p3 = re.compile(date_3)
    match = p3.finditer(str(date))
    for x in match:
        print('Date found : ',x)
    date_4 = r'^\d{4}-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$'
    p4 = re.compile(date_4)
    match = p4.finditer(str(date))
    for x in match:
        print('Date found : ',x)
        
