import sys
import math
n= int(sys.stdin.readline())
data = tuple(map(int, sys.stdin.readline().split()))
min_num = min(data)


a=1
for d in data:
  a =a*d//(math.gcd(a,d))

if a in data:
  print(min_num*a)
else:
  print(a)