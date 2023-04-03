n=int(input())
l=[]
for i in range(n):
    s=int(input())
    m=[]
    for j in range(s+1):
        for k in range(s+1):
            u=j+2*k
            if u==s:
                m.append([j,k])
    l.append(m)
from math import factorial as f
c=0

for j in l:
    c=0
    for i in j:
        k=i[0]+i[1]
        u=f(k)
        p=(f(i[0])*f(i[1]))
        c=c+u//p
    print(c)
