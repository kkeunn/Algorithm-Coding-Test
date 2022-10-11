import sys

X = int(sys.stdin.readline())

d = [0] * (X+1)

for i in range(2, X+1):
    # 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[X])
