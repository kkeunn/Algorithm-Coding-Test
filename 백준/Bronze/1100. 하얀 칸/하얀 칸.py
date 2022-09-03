import sys


odd_row = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
even_row = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
count = 0
for i in range(1, 9):
    board = list(sys.stdin.readline())
    if i % 2 == 0:
        a = list(map(lambda x, y: x*y, board, even_row))
        count += a.count('F')
    else:
        a = list(map(lambda x, y: x*y, board, odd_row))
        count += a.count('F')
print(count)