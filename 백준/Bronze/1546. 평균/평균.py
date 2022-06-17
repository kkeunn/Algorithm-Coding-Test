n = int(input())
test_list = list(map(int, input().split()))
m = max(test_list)

for i in range(len(test_list)):
  test_list[i] = test_list[i]/m*100
test_avg = sum(test_list)/n
print(test_avg)