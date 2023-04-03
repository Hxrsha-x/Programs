#Binary Files
import pickle as p
def create():
    f=open('item.dat','ab')
    l=[]
    while True:
        l1=eval(input('enter the item no.,name,price,qty'))
        l.append(l1)
        ch=input('countinue?(Y/N)')
        if ch.upper()!='Y':
            break
    p.dump(l,f)
    f.close()
def display():
    f=open('item.dat','rb')
    while True:
        try:
            s=p.load(f)
            cost=0
            for i in s:
                c=i[2]*i[3]
                cost=cost+c
        except EOFError:
            break
    print('the total cost of puschase is',cost)
    f.close()
create()
display()
