import sys
n = int(sys.stdin.readline())

result = 1000000
for i in range(n):
  a = list(map(int,list(str(i))))
  b = i + sum(a)
  if b == n:
    result = min(result, i)


print(result if result != 1000000 else 0)