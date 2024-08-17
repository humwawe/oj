n, m, k = map(int, input().split())
lim = 1 << n
dp = [[0] * lim for _ in range(m)]

for i in range(lim):
  dp[0][i] = 1

mod = 998244353


def f(x):
  return bin(x).count("1")


bit_count = [0] * lim
for i in range(1, lim):
  bit_count[i] = f(i)

for i in range(1, m):
  for pre in range(lim):
    for cur in range(lim):
      if bit_count[pre & cur] >= k:
        dp[i][cur] = (dp[i][cur] + dp[i - 1][pre]) % mod

res = 0
for i in range(lim):
  res = (res + dp[m - 1][i]) % mod

print(res)
