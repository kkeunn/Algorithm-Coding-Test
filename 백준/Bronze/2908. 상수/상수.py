import sys
a, b = map(int, sys.stdin.readline().split())
a, b="".join(reversed(str(a))), str(b)[::-1]
print(a if a>b else b)