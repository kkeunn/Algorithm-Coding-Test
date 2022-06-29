import sys
n, m= map(int,sys.stdin.readline().split())
a_set = set(map(int,sys.stdin.readline().split()))
b_set = set(map(int,sys.stdin.readline().split()))

print(len(b_set-a_set)+len(a_set-b_set))