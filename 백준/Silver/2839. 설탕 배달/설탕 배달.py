n = int(input()) 
b = 0 
while n >= 0:
    if n % 5 == 0:
        b += n // 5
        print(b)
        break
    n -= 3
    b += 1
else:
    print(-1)
# while else
# 조건식이 거짓으로 판정되어 수행되지 않을 때 else 절
# break에 의해 반복문이 끝나면 else 절 수행 X