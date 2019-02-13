import re
def stripComments(code):
    code = str(code)
    return re.sub(r'(?m)^*#.*\n?',"",code)
    print(stripComments("""#foobar bar foo # buz"""))
