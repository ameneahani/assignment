def checker_board(n,m):
    for row in range (n):
        for column in range(m):
            if (row % 2==0 and column % 2==0) or (row %2 !=0 and column %2 !=0 ):
                print("#",end="")
            else:
                print("*",end="")
        print("")

n=int(input("enter the number of rows, n:"))
m=int(input("enter the number of columns, m:"))
checker_board(n,m)



