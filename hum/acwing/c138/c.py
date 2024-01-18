n = int(input())
a = list(map(int, input().split()))
sa = sum(a)
dp = [[0] * (2 * sa + 1) for _ in range(n)]
dp[0][a[0] + sa] += 1
dp[0][-a[0] + sa] += 1
mod = 10 ** 9 + 7
for i in range(1, n):
  dp[i][a[i] + sa] += 1
  dp[i][-a[i] + sa] += 1
  for e in range(0, 2 * sa + 1):
    if dp[i - 1][e]:
      dp[i][e + a[i]] += dp[i - 1][e]
      dp[i][e - a[i]] += dp[i - 1][e]
      dp[i][e + a[i]] %= mod
      dp[i][e - a[i]] %= mod

print(sum(dp[i][sa] for i in range(n)) % mod)
