import sys
n, k = map(int, sys.stdin.readline().split())

coin_list = []
for _ in range(n):
    coin_list.append(int(sys.stdin.readline().rstrip()))

result = 0
for coin in sorted(coin_list, reverse = True):
    if k // coin != 0:
        result +=  k // coin
        k = k % coin
print(result)