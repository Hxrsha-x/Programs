#
m=input()
n=input()
p=input()
q=input()
w=[]

for i in range(int(m)):
    w.append(input().split())
l=input()
f=w.copy()
if l!=p:
    e=p
else:
    e=q
print(e)
k=0
for i in f:
    v=0
    for j in i:
        o=[]
        u=[]
        if j==l:
            for i in range(int(n)):
                o.append(w[k][i])
            for i in range(int(m)):
                u.append(w[i][v])
            o.extend(u)
            if e in o :
                f[k][v]=e
            if w==f:
                print('How....................')
        v+=1
    k+=1
print(f)
print(w)
