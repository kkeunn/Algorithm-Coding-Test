import sys
x, y, w, h = map(int,sys.stdin.readline().split())
d = min((w-x),(h-y), x, y)
print(d)