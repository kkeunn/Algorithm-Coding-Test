import sys
n,m  = map(int, sys.stdin.readline().split())
a_set = set()
b_list = []
for _ in range(n):
  a_set.add(sys.stdin.readline().strip())

for _ in range(m):
  b_list.append(sys.stdin.readline().strip())

cnt = 0
for b in b_list:
  cnt += (1 if b in a_set else 0)
print(cnt)