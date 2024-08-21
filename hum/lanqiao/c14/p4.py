from math import inf

n = int(input())
v = list(map(int, input().split()))
m = max(v)
b = list(map(int, input().split()))
a = list(map(int, input().split()))
dp = [[inf] * (m + 1) for _ in range(n)]
dp[0][v[0]] = 0
dp[0][min(v[0] + a[0], m)] = min(dp[0][min(v[0] + a[0], m)], b[0])
for i in range(1, n):
  for j in range(m, v[i] - 1, -1):
    dp[i][j] = min(dp[i][j], dp[i - 1][j])
    dp[i][min(j + a[i], m)] = min(dp[i][min(j + a[i], m)], dp[i][j] + b[i])

res = min(dp[-1])
if res == inf:
  print(-1)
else:
  print(res)
