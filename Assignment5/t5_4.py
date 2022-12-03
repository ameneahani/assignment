#definition of Pascal triangle
def pascal (n):
    A=[]
    B=[]
    A.append(1)
    B.append(1)

    for i in range (n-1):
        A.append(0)
        B.append(0)
    for row in range (1,n+1):
        print(B[0],end=" ")
        for column in range (row-1):
            B[column+1]=A[column+1]+A[column]
            if B[column+1] != 0:
                print(B[column+1],end=" ")
        print("")
        for i in range (n):
            A[i]=B[i]

pascal (int(input("n = ")))
    

