import sys
x_square = []
y_square = []
for _ in range(3):
  x, y = map(int,sys.stdin.readline().split())
  if x in x_square:
    x_square.remove(x)
  else:
    x_square.append(x)
  if y in y_square:
    y_square.remove(y)
  else:
    y_square.append(y)

print(x_square[0],y_square[0])