import sys
n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]
count = []

for a in range(n-7):
    for b in range(m-7):
        w_start = 0
        b_start = 0 
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        w_start += 1
                    if board[i][j] != 'B':
                        b_start += 1
                else:
                    if board[i][j] != 'B':
                            w_start += 1
                    if board[i][j] != 'W':
                        b_start += 1
        count.append(min(w_start, b_start))
print(min(count))