t = int(input())

for _ in range(t):
  k = int(input())
  n = int(input())
  lst = [x for x in range(1, n+1)]
  
  for f in range(k):
    for i in range(1, n):
      lst[i] += lst[i-1]

  print(lst[-1])