T = int(input())
num_list = []
for _ in range(T):
  N = int(input())
  num_list.append(N)

for i in range(len(num_list)):
  for j in range(i+1,len(num_list)):
    if num_list[i] >= num_list[j]:
      num_list[i],num_list[j] = num_list[j],num_list[i]

for num in num_list:
  print(num)