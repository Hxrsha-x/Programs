#Program to find Unique Rectangular Dimension
n=int(input())
l=[]
k=0
for i in range(1,n//2+2):
    if n%i==0:
        l.append(i)
for j in l:
    if j<=n//j:
        k+=1
print(k)
for j in l:
    if j<=n//j:
        print(j,n//j)
