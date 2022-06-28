import sys
n = int(input())

words= []
for _ in range(n):
  words.append(sys.stdin.readline().strip())
# sys.stdin.readline()은 \n을 포함하는 입력
  
words = list(set(words))
words.sort(key=lambda x: (len(x),x))
for word in words:
  print(word)