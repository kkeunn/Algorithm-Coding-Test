import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
  num_list.append(int(sys.stdin.readline()))
  
print(round(sum(num_list) / n))
num_list.sort()
print(num_list[n//2])
cnt = Counter(num_list)
tmp = cnt.most_common()

if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])

print(max(num_list) - min(num_list))