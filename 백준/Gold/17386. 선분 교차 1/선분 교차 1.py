import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
A, B, C, D = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c 
    return x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)

if ccw(A, B, C) * ccw(A, B, D) <= 0  and ccw(C, D, A) * ccw(C, D, B) <= 0:
    print(1)
else:
    print(0)