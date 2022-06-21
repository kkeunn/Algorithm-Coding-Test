#1: 1개
#2~7: 6개
#8~19: 12개
#20~37: 18개
#38~61: 24개
# lst = [[1], [2,3,4,5,6,7],[8,9,10,11,12,...],...]

num = int(input())
lst = [[1]]
a = 2
n = 1
while num >= a:
  lst.append([a])
  # for i in range(a, a+6*n):
  #   if i==a:
  #     lst.append([i])
  #   else:
  #     lst[n].append(i)
  a=a+6*n
  n+=1

print(len(lst))