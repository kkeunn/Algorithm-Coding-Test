import sys
h, m = map(int, sys.stdin.readline().split())
cost  = int(input())
t = (h*60+m+cost-1440 if h*60+m+cost >= 1440 else h*60+m+cost)
print(t//60, t-60*(t//60) )