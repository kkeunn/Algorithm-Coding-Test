import sys
n = int(sys.stdin.readline())
a_card = [*map(int, sys.stdin.readline().split())]
a_set = set(a_card)
m = int(sys.stdin.readline())
b_card = [*map(int, sys.stdin.readline().split())]
count = {}
for a in a_card:
  if a in count:
    count[a] += 1
  else:
    count[a] = 1

for b in b_card:
  result = count.get(b)
  if result == None:
    print(0, end=" ")
  else:
    print(result, end=" ")