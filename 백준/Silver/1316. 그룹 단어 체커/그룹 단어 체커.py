n = int(input())

cnt = 0
for _ in range(n):
  word = input()
  alphabet = list(set(word))
  flag = 0
  for a in alphabet:
    if word[word.index(a):word.index(a)+word.count(a)]!=a*word.count(a):
      flag = 1
  if flag==0:
    cnt+=1
print(cnt)