word = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

cnt = len(word)
for c in croatia:
  if c in word:
    cnt-=word.count(c)
print(cnt)