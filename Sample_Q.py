'''Arvind has created a dictionary containing names of cities and total parks (integer) as key, value pair of 5 cities.
Write a program with separate user defined function to perform the following operations:
a. Push the keys of the dictionary into a stack where the corresponding value of total parks is greater than 10.
b. Pop and display the contents of the stack.'''
d=eval(input('enter the city, no. of parks'))
stk=[]
def push(D,stk):
    for i in D:
        if D[i]>10:
            stk.append(i)
    return stk
def pop(stk):
    if stk==[]:
        print('stack underflow')
    else:
        while stk!=[]:
            p=stk.pop()
            print(p,end=" ")
push(d,stk)
pop(stk)
