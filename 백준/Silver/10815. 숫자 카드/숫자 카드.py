import sys
n = int(sys.stdin.readline())
a_list = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b_list = list(map(int,sys.stdin.readline().split()))
result=""
for b in b_list:
  result += ("1 " if b in a_list else "0 ")
print(result[:-1])