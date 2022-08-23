import sys

n, k = map(int, sys.stdin.readline().split())

temperature = list(map(int, sys.stdin.readline().split()))
max_temp = 0
t = []
t.append(sum(temperature[:k]))

for i in range(0,n-k):
    t.append(t[i]-temperature[i] + temperature[i+k])
  
print(max(t))