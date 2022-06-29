import sys
string = sys.stdin.readline().strip()
word_set = set()
for i in range(len(string)):
  for j in range(i,len(string)):
    word_set.add(string[i:j+1])
  
print(len(word_set))