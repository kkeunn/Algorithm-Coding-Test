import sys

while 1:
  square = set(map(lambda x: int(x)**2, sys.stdin.readline().split()))
  if square == {0,0,0}:
    break
  max_l = max(square)
  square.remove(max_l)
  print("right" if max_l == sum(square) else "wrong")
  