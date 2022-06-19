def d(num):
 
  total=num
  num = str(num)
  for n in num:
    total+=int(n)
  return total

lst1 = set()
lst2 = set(range(1, 10000+1))
for l in range(1, 10000+1):
  lst1.add(d(l))

for l in sorted(lst2-lst1):
  print(l)