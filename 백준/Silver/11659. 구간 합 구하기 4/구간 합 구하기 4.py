import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

dp=[0]*(n+1)
for k in range(1,n+1):
    dp[k]=dp[k-1]+arr[k-1]
for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    print(dp[j]-dp[i-1])