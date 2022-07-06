import sys
n = int(sys.stdin.readline())

xy_list = []
for _ in range(n):
  xy = tuple(map(int, sys.stdin.readline().split()))
  xy_list.append((xy))

rank = []
for i in range(n):
  count = 1
  for j in range(n):
    if xy_list[i][0] < xy_list[j][0] and xy_list[i][1] < xy_list[j][1]:
      count+=1
  rank.append(count)
      

for i in rank:
  print(i, end=" ")
    