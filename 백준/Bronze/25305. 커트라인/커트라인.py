import sys
n, c = map(int,sys.stdin.readline().split())

score_list = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)
print(score_list[c-1])