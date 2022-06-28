import sys
n = int(sys.stdin.readline())

x_list = list(map(int,sys.stdin.readline().split()))
x_set = sorted(list(set(x_list)))
result = {}
for i in range(len(x_set)):
  result[x_set[i]] = i
for x in x_list:
  print(result[x], end =" ")