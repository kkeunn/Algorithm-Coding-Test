import sys
T = int(sys.stdin.readline())
num_list = []
for _ in range(T):
  N = int(sys.stdin.readline())
  num_list.append(N)
  
for num in sorted(num_list):
  print(num)