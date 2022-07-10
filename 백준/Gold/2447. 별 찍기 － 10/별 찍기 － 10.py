def star_recursive(n):
  if n == 1:
    return ['*']

  star = star_recursive(n//3)
  star_list = []

  for s in star:
    star_list.append(s*3)
  for s in star:
    star_list.append(s+' '*(n//3)+s)
  for s in star:
    star_list.append(s*3)
  
  return star_list

n=int(input())
print('\n'.join(star_recursive(n)))