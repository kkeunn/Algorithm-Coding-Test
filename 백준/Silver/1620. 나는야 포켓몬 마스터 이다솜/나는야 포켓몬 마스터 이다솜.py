import sys
n,m  = map(int, sys.stdin.readline().split())
pocket_dic_num = {}
pocket_dic_alpha = {}
for i in range(1,n+1):
  p = sys.stdin.readline().strip()
  pocket_dic_num[i] = p
  pocket_dic_alpha[p] = i
  
for _ in range(m):
  q = (sys.stdin.readline().strip())
  try:
    q = int(q)
    print(pocket_dic_num[q])
  except:
    print(pocket_dic_alpha[q])
    