import re
def isValidcurr(curr):
    c1 = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    p1 = re.compile(c1)
    match = p1.finditer(str(curr))
    for x in match:
        print('currency found : ',x)
    c2= r'^-?\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    p2 = re.compile(c2)
    match = p2.finditer(str(curr))
    for x in match:
        print('currency found : ',x)
    c3= r'^\+?\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    p3 = re.compile(c3)
    match = p3.finditer(str(curr))
    for x in match:
        print('currency found : ',x)
    c4= r'^USD\d+(\.\d+)?[KMB]?$'
    p4 = re.compile(c4)
    match = p4.finditer(str(curr))
    for x in match:
        print('currency found : ',x)
    c5= r'^\$\d+(\.\d+)?[KMB]?$'
    p5 = re.compile(c5)
    match = p5.finditer(str(curr))
    for x in match:
        print('currency found : ',x)