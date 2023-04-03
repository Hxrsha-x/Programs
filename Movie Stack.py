#Stack
def push(l):
    a=eval(input('enter movie name , year of release'))
    l.append(a)
    print('CDHOLDER contains')
    for i in l[::-1]:
        print(i)
def pop(l):
    p=l.pop()
    print('element popped:',p)
    for i in l[::-1]:
        print(i)
CDHOLDER=eval(input('enter the movie list'))
push(CDHOLDER)
pop(CDHOLDER)
