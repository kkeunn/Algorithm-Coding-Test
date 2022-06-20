words = input().upper()
cnt_word = list(set(words))
lst =[]
for i in cnt_word:
  lst.append(words.count(i))

if lst.count(max(lst))>1:
  print("?")
else:
  print(cnt_word[lst.index(max(lst))])