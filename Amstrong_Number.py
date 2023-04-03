#To check if a number is an Amstrong number
n=int(input())
s=str(n)
l=len(s)
c=0
for i in s:
    c+=int(i)**l
if c==n:
    print('amstrong')
else:
    print('not amstrong')
