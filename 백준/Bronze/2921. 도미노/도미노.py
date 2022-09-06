import sys

N = int(sys.stdin.readline().rstrip())
point = N + 2
result = 1 * point

for i in range(2, N+1):
    result += i * point
print(result)