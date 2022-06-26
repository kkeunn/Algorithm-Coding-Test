# 카운팅 정렬, 시간복잡도: O(n + k) 
import sys
t = int(sys.stdin.readline())

countring_list =[0 for _ in range(10001)]
for _ in range(t):
  n = int(sys.stdin.readline())
  countring_list[n] += 1
  
for n in range(1, 10001):
  cnt = countring_list[n]
  for _ in range(cnt):
        print(n)