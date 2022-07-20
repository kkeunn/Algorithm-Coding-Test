import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    rs = r1+ r2
    rd = max(r1, r2) - min(r1, r2)

    # 만나지 않는 경우->0
    if d > rs:
        print(0)
    # 원이 외접하는 경우-> 1
    elif d == rs:
        print(1)
    # 겹치는 경우-> 2
    elif rd < d < rs:
        print(2)
    # 원이 같은 경우-> -1
    elif rd == 0 and d == 0:
        print(-1)
    # 내접하는 경우-> 1
    elif rd == d:
        print(1)
    # 원이 내부에 있는 경우-> 0
    else:
        print(0)
        
    


