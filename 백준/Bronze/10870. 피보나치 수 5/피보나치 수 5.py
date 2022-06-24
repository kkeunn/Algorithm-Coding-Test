def Fibonacci(n):
  if n == 0:
    result = 0
  elif n == 1:
    result =1
  else:
    result =  Fibonacci(n-1) +Fibonacci(n-2)
  return result

n = int(input())
print(Fibonacci(n))