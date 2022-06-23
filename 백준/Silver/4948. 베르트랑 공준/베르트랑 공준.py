def prime_list(N,M):
    sieve = [False,False]+[True] * (N-1)

    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, N+1, i): 
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(M+1, N+1) if sieve[i] == True]

while 1:
  M = int(input())
  N = 2*M
  if M==0:
    break
  p_list = prime_list(N,M)
  
  print(len(p_list))
