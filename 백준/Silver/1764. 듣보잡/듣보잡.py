import sys
n, m = map(int,sys.stdin.readline().split())
a_set = set()
b_set = set()
for _ in range(n):
  a_set.add(sys.stdin.readline().strip())
for _ in range(m):
  b_set.add(sys.stdin.readline().strip())

c_set = a_set.intersection(b_set)
print(len(c_set))
for c in sorted(list(c_set)):
  print(c)