#Pancard Checker
s=input()
if len(s)==10:
    a=s[0:5]
    b=s[5:9]
    c=s[9]
    a=a+c
    if a.isalpha():
        if a.isupper():
            p=True
        else:
            p=False
    if b.isdigit():
        q=True
    else:
        q=False
    if p and q:
        print('valid')
    else:
        print('invalid')
else:
    print('invalid')
