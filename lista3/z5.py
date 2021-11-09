import re
p= input("Podaj hasło: ")
x = True
while x:  
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Poprawne hasło")
        x = False
        break

if x:
    print("Niepoprawne hasło")

