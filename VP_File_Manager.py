#File Manager
n=int(input())
m=int(input())
z=[]
for i in range(m):
    w=input().split()
    u=[]
    for j in w:
        u.append(int(j))
    z.append(u)
fn=input().split()
Q=int(input())
q=[]
for i in range(Q):
    query=input().split()
    q.append(query)
d={}
for i in range(1,len(fn)+1):
    l=[]
    for j in z:
        if j[0]==i:
            l.append(fn[j[1]-1])
    if fn[i-1][-4:]!=".txt":
        d[fn[i-1]]=l
for i in range(Q):
    w=q[i][1].split("/")
    w.remove(w[0])
    if w[0]=="":
        w.remove(w[0])
        w.append("/")
    for j in d:
        if j==w[-1]:
            if q[i][-1] in d[j]:
                print("no")
                break
            else:
                '''h=d[j].copy()        #Adding the file in the destination (Not required in this question as they have just asked the possibility)
                h.append(q[i][-1])
                d[j]=h
                u=q[i][0].split("/")    #Removing the file from the source (Not required in this question)
                u.remove(u[0])
                if u[0]=="":
                    u.remove(u[0])
                    u.append("/")
                for j in d:
                    if j==u[-1]:
                        g=d[j].copy()
                        g.remove(q[i][-1])
                        d[j]=g'''
                print("yes")
                break
