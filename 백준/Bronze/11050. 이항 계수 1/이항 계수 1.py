from math import factorial
import sys

n, k = map(int,sys.stdin.readline().split())
result = factorial(n) // (factorial(k) * factorial(n - k))

print(result)