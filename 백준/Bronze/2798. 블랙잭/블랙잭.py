import sys
n, m = map(int,sys.stdin.readline().split())

card_list = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      total = card_list[i] + card_list[j] + card_list[k]
      if total > m:
        continue
      else:
        result = max(result,total)
print(result)