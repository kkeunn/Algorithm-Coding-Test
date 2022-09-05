import sys
N, Q = map(int, sys.stdin.readline().split())
sheet = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
for _ in range(Q):
    t = int(sys.stdin.readline().rstrip())
    for i in range(N):
        if t < sum(sheet[:i+1]):
            print(i+1)
            break