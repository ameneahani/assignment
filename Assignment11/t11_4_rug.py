def generate_rug(n):
    B = []
    imoji = ['🐧','🐛','🦜','🦢','🐦','🕊️','🦩','🦉','🐝','🪰','🦇','🐞','🦋']
    for i in range (n):
        A = list(imoji[n//2+1] for i in range(n))
        B.append(A)
    for k in range (n//2):
        for i in range(1+k,n-1-k):
            for j in range(1+k,n-1-k):
                B[i][j] = imoji[k]
    for line in B:
        print(line)

a = int(input())
if a % 2 == 0:
    print("cant draw a rug with even number!")
else:
    generate_rug(a)
