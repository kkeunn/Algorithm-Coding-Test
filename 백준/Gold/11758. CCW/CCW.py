import sys

x_list = []
y_list = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)
x_list.append(x_list[0])
y_list.append(y_list[0])
a = sum(map(lambda x, y: x * y, x_list[:-1], y_list[1:]))
b = sum(map(lambda x, y: x * y, x_list[1:], y_list[:-1]))
if a-b > 0:
    print(1)
elif a-b < 0:
    print(-1)
else:
    print(0)