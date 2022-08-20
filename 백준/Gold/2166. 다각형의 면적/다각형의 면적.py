import sys

n = int(sys.stdin.readline().rstrip())
x_list = []
y_list = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)
x_list.append(x_list[0])
y_list.append(y_list[0])
a = sum(map(lambda x, y: x * y, x_list[:-1], y_list[1:]))
b = sum(map(lambda x, y: x * y, x_list[1:], y_list[:-1]))
print(round(abs(a-b)/2,1))