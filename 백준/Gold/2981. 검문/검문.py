import sys
import math

n = int(sys.stdin.readline())
num_list =[]
num_list.append(int(sys.stdin.readline().rstrip()))
for i in range(1,n):
  num_list.append(int(sys.stdin.readline().rstrip()))
  if i == 1:
    gcd = abs(num_list[1] - num_list[0])
  gcd = math.gcd(abs(num_list[i] - num_list[i-1]), gcd)

m_list = []
for i in range(2, int(gcd**0.5)+1):
  if gcd % i == 0:
    m_list.append(i)
    m_list.append(gcd//i)
m_list.append(gcd)
m_list = set(m_list)
print(*sorted(m_list))