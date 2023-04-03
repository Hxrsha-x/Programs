#Time in Heaven converter
L=input().split()
k=L[0]
x=k.split(':')
i=''
if L[1]=='A.M' and x[0]!='12':
    i=k
elif x[0]=='12' and k!='12:00:00':
    i='00'+':'+x[1]+':'+x[2]
elif L[1]=='P.M':
    i=str(int(x[0])+12)+':'+x[1]+':'+x[2]
elif L[1]=='midnight':
    i='00:00:00'
else:
    i='12:00:00'
o=i.split()
h=o[0].split(':')
y=int(h[0])
if y<8 and o[0]!='00:00:00':
    g='0'+str(y)+':'+h[1]+':'+h[2]+' A.M'
elif i=='08:00:00':
    g='08:00:00 midmorning'
elif y>=8 and i!='08:00:00' and y<16:
    g='0'+str(y-8)+':'+h[1]+':'+h[2]+' B.M'
elif i=='16:00:00':
    g='08:00:00 midevening'
elif y>=16 and i!='16:00:00' and y<24:
    g='0'+str(y-16)+':'+h[1]+':'+h[2]+' C.M'
else:
    g='08:00:00 midnight'
print(g)
