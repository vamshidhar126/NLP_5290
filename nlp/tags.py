import re

def isTag(line):
    patn = re.compile(r'<(\w+)\s*.*?[^\/]>')
    match = patn.finditer(line)
    for x in match :
        print("Found tag : ",x)
        return True
    return False