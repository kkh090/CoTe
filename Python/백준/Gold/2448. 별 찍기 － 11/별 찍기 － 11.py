N = int(input()) // 3

piece = ["  *  ",
         " * * ",
         "*****"]

n = 0

temp= []

while N != 1:
    N = N // 2
    n += 1


for i in range(n, 0, -1): 
    
    t = len(piece)
    for j in range(t):
        piece.append(piece[j] + " " + piece[j])
        piece[j] = " " * t + piece[j] + " " * t

for p in piece:
    print(p)
