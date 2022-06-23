N = int(input())
num = N
for n in range(2,N+1):
  if num%n==0:
    while num%n==0:
      num/=n
      print(n)
  if num==1:
    break