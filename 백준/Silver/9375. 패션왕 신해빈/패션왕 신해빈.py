import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  clothes_dict = {}
  for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if b in clothes_dict:
      clothes_dict[b] +=1
    else:
      clothes_dict[b] = 2

  value_list = tuple(clothes_dict.values())

  result = 1
  for value in value_list:
    result *= value
  print(result-1)