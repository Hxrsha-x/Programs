#Christmas Tree pyramid
n = int(input("Enter the number of rows"))  
for i in range(0, n):  
    t=' '*(n-i)
    print(t)
    for j in range(0, i + 1):  
        print(" * ", end=" ")       
    print()  
