import sys

T = int(input())

for _ in range(T):
  H,W,N = map(int, sys.stdin.readline().split())
  y = N%H
  x = N//H+1
  if y == 0:
    y = H
    x -= 1

  print(y*100+x)