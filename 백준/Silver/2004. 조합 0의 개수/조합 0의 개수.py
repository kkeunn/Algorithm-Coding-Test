import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def count2(N):
    count = 0
    while N != 0:
        N = N//2
        count += N
    return count

def count5(N):
    count = 0
    while N != 0:
        N = N//5
        count += N
    return count

two_count = count2(n) - count2(n-m) - count2(m)
five_count = count5(n) - count5(n-m) - count5(m)
print(min(two_count, five_count))