import sys
n = int(input())

xy_list = []
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  xy_list.append((x,y))

xy_list.sort(key=lambda x: (x[1], x[0]))
for xy in xy_list:
  print(xy[0],xy[1])