def n_and_m(n, m):
    if len(answer) == m:
        print(' '.join(map(str, answer)))

    for i in range(1, n+1):
        if not answer and len(answer) != n:
            answer.append(i)
            n_and_m(n, m)
            answer.pop()
        elif answer and len(answer) != n and answer[-1] <= i:
            answer.append(i)
            n_and_m(n, m)
            answer.pop()
    

n, m = map(int, input().split())
answer = []

n_and_m(n, m)