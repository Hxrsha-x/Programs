#To check mobile number
n=input()
if len(n)==10:
    if n[0]!='0':
        if n.isdigit():
            print("valid")
        else:
             print("not valid")
    else:
         print("Not valid")
else:
    print("not valid")
