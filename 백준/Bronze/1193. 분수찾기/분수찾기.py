x = int(input())

diagonal = 1

while x > diagonal:
  x -= diagonal
  diagonal += 1

if diagonal % 2 == 0:
  a = x
  b = diagonal - x + 1

else:
  a = diagonal - x + 1
  b = x

print(f"{a}/{b}")