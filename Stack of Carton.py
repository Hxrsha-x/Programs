#Stack of Carton
def pushcarton(l):
    a=eval(input('enter carton number,date of arrival'))
    l.append(a)
def popcarton(l):
    if len(l)==0:
        print('underflow')
    else:
        p=l.pop()
        print('the element popped is',p)
def displaycarton(l):
    if len(l)==0:
        print('underflow')
    else:
        for i in l[::-1]:
            print(i)
def peek(l):
    if len(l)==0:
        print('underflow')
    else:
        t=len(l)-1
        print('the element at the top of stack is',l[t])
def ship(l):
    l.clear()
    print('all cartons are shipped')
    print(l)
warehouse=eval(input('enter the list of cartons'))
print('''enter your choice
         1.push
         2.pop
         3.display
         4.peek
         5.shipping catoons
         6.exit''')
while True:
    ch=int(input('enter your choice'))
    if ch==1:
        pushcarton(warehouse)
    elif ch==2:
        popcarton(warehouse)
    elif ch==3:
        displaycarton(warehouse)
    elif ch==4:
        peek(warehouse)
    elif ch==5:
        ship(warehouse)
    else:
        print('exit')
        break
