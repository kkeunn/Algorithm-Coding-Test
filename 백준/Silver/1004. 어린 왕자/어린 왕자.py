import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().rstrip())
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        if (x1 - cx)**2 + (y1 - cy)**2 < r**2 < (x2 - cx)**2 + (y2 - cy)**2 or (x2 - cx)**2 + (y2 - cy)**2 < r**2 < (x1 - cx)**2 + (y1 - cy)**2:
            count += 1

    print(count)