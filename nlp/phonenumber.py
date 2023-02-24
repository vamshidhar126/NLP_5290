import re
def isValidphn(pn):
    pn1 = r'^\d{10}$'
    p1 = re.compile(pn1)
    match = p1.finditer(str(pn))
    for x in match:
        print('phone number found : ',x)
    pn2 = r'^\+\d{1,3}\s\d{3}\s\d{3}-\d{4}$'
    p2 = re.compile(pn2)
    match = p1.finditer(str(pn))
    for x in match:
        print('phone number found : ',x)
    pn3 = r"\(\d{3}\)-\d{3}-\d{4}"
    p1 = re.compile(pn3)
    match = p1.finditer(str(pn))
    for x in match:
        print('phone number found : ',x)
    pn4 = r"\d{3}-\d{3}-\d{4}"
    p1 = re.compile(pn4)
    match = p1.finditer(str(pn))
    for x in match:
        print('phone number found : ',x)
