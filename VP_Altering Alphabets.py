#Reordering alphabets according to the conditions
s1=input()
s2=input()
s1=s1[::2]
s2=s2[1::2]
l1=list(s1)
l2=list(s2)
l2.append('')
s3=''
for i in range(len(s1)):
        s3+=chr(ord(l1[0])+1)+chr(ord(l2[0])+1)
        l1.pop(0)
        l2.pop(0)
print(s3)
