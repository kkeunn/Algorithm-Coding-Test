n=int(input())

def hansu(n):
  if n < 100:
    han = n
  else:
    han = 99
    for i in range(100, n+1):
      m=str(i)
      if int(m[0])-int(m[1]) == int(m[1])-int(m[2]):
        han+=1
  return han

print(hansu(n))