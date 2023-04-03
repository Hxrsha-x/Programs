#Stack - Push and Pop
R={"OM":76, "JAI":45, "BOB":89,"ALI":65, "ANU":90, "TOM":82}
stk=[]
def push(stk,R):
    for i in R:
        if R[i]>75:
            stk.append(i)
def POP(stk):
    while stk!=[]:
        p=stk.pop()
        print(p,end=" ")
push(stk,R)
POP(stk)
