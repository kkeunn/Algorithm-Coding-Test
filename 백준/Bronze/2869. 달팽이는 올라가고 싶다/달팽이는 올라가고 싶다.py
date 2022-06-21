import sys
a,b,v = map(int, sys.stdin.readline().split())

d=(v-b)/(a-b)
print(int(d) if d == int(d) else int(d)+1)