def prime_list(N,M):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [False,False]+[True] * (N-1)

    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, N+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(M, N+1) if sieve[i] == True]

M = int(input())
N = int(input())

p_list = prime_list(N,M)
if len(p_list)<=0:
  print(-1)
else:
  print(sum(p_list))
  print(min(p_list))