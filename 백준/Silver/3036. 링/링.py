import sys
import math

n = int(sys.stdin.readline())
data = tuple((map(int,sys.stdin.readline().split())))

for i in range(1,n):
  a = math.gcd(data[0], data[i])
  print(f'{data[0]//a}/{data[i]//a}')