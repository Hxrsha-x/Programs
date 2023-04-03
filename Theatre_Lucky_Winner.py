w=input()
n=int(input())
s=w*n
l=list(s)
print(l)
for i in range(1,n+1):
    t=l[i-1]
    v=l[2*n-i]
    if t==v:
        g=i
print(g)
