import sys
n = int(input())
for _ in range(n):
  re, string = map(str, sys.stdin.readline().split())
  for s in string:
    print(s*int(re), end="")
  print()