
def multiplication_table(rows:int,columns:int):
    for i in range(rows):
        for j in range(columns):
            print((i+1)*(j+1),end="  ")
        print("")

n=int(input("enter the number of rows, n:"))
m=int(input("enter the number of columns , m:") )

multiplication_table(n,m)