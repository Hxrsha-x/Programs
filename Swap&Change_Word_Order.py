#To reverse the order of the words and swap their letter cases
sentence=str(input())
s=sentence[::-1]
l=s.split()
k=''
a=[]
def reverse_words_order_and_swap_cases(l,k,a):
    for i in l:
        for j in i:
            t=j.isupper()
            if t:
                k=k+j.lower()
            else:
                k=k+j.upper()
        a.append(k)
        k=''
reverse_words_order_and_swap_cases(l,k,a)
for i in a:
    print(i,end=' ')
