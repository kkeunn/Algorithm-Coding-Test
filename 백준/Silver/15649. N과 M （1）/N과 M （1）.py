def n_and_m(n, m):

  if len(answer) == m:
    print(' '.join(map(str, answer)))

  for i in range(1, n+1):
      if i not in answer:
            answer.append(i)
            n_and_m(n, m)
            answer.pop()

n, m = map(int, input().split())
answer = []

n_and_m(n, m)