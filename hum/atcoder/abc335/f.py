n = int(input())
a = list(map(int, input().split()))
mod = 998244353
M = 500
d = [[0] * M for i in range(M)]

dp = [0] * n
dp[0] = 1

for i in range(n):
  for j in range(1, M):
    dp[i] += d[j][i % j]
  dp[i] %= mod
  if a[i] >= M:
    for j in range(i + a[i], n, a[i]):
      dp[j] += dp[i]
      dp[j] %= mod
  else:
    d[a[i]][i % a[i]] += dp[i]
    d[a[i]][i % a[i]] %= mod

print(sum(dp) % mod)
