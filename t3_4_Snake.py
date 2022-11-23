# Draw a snake with lenth of n
n=int(input("enter lenth of  the snake:"))
snake=[]
for i in range(n):
    if i % 2 ==0:
        snake.append("*")
    else:
        snake.append("#")
    print(snake[i],end="")       