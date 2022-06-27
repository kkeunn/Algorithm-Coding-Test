N = list(map(int,input()))

N.sort(reverse=True)
N = list(map(str,N))
print(int("".join(N)))