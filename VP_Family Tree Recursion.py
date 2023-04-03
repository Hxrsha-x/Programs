n=int(input())
tok=input().split(" ")
d={}
for i in range(n-1):
    x=input().split(" ")
    if int(x[0]) not in d:
        d[int(x[0])]=[int(tok[int(x[1])-1])]
    else:
        d[int(x[0])].append(int(tok[int(x[1])-1]))

q=int(input())
qs=[]
for i in range(q):
    a=int(input())
    qs.append(a)
def isprime(n):
    if(n==1):
        return False
    elif n==2:
        return True
    else:
        for i in range(2, int(n**1/2+1)):
            if n%i ==0:
                return False
        else:
            return True
def child(n):
    if (n not in d) or (d[n] in l2):
        return 
    else:
        for j in d[n]:
            if isprime(j):
                l2.append(j)
            child(j)
#print(qs)
for i in qs:
    l2=[]
    child(i)
    print(len(l2))
