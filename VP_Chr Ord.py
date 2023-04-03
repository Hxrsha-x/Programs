a=ord('a')
n=ord('n')
d={}
for i in range(13):
    d[chr(a)]=chr(n)
    a+=1;n+=1
w=input()
l=list(w)
t=l.copy()
l1=[]
l2=[]
r=0
if len(l)%2==0:
    for i in l:
        if i in d.keys():
            if d[i] in l:
                t.remove(i)
                t.remove(d[i])
    if t==[]:
        for i in l:
            if i in d:
                l1.append(i)
                u=l.index(i)
                w=l.index(d[i])
                if u<w:
                    y=True
                else:
                    y=False
            else:
                l2.append(i)
    if y:
        r+=1
        for i in l1:
            q=l2.index(d[i])
            e=l1.index(i)
            p=l2[e-r]
            if q<p:
                y=True
            elif l.index(i)==l.index(d[i])-1:
                y=False
            else:
                y=False
                break
