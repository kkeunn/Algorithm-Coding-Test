import sys
n = int(input())

users= []
for i in range(n):
  year, name = map(str,sys.stdin.readline().split())
  users.append((int(year),name,i))
  
users.sort(key=lambda x: ((x[0]),x[2]))
for user in users:
  print(user[0],user[1])