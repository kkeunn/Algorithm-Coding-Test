def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
  
t = int(input())

for _ in range(t):
  n = int(input())
  lst = prime_list(n) 
  i = n//2
  j = n//2 + 1
  while 1:
    if i in lst and n-i in lst:
      print(i, n-i)
      break
    if j in lst and n-j in lst:
      print(n-j, j)
      break
  
    i-=1
    j+=1