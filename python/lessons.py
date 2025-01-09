"""n = int(input("Enter the value of n: "))
for i in range (n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range (i+1):
        print("#",end="")
    print()
    """
    
"""for i in range (n):
    print(" "*(n-i-1) + "*"*(i+1))
            """

num_rows = int(input("Enter the number of rows: "))
for i in range (0,num_rows):
    for j in range(num_rows-i-1):
        print(end=" ")
    for j in range (0,i+1):
        print("*",end="")
    print()    
    