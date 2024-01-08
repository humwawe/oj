from math import inf

n, m, b = map(int, input().split())
e = []
for _ in range(n):
  x, k, _ = map(int, input().split())
  st = 0
  a = list(map(int, input().split()))
  for i in a:
    st |= 1 << i - 1
  e.append((x, k, st))

e.sort(key=lambda x: x[1])

dp = [inf] * (1 << m)
dp[0] = 0
res = inf
for i in range(n):
  for st in range((1 << m) - 1, -1, -1):
    nst = st | e[i][2]
    dp[nst] = min(dp[nst], dp[st] + e[i][0])

  res = min(res, dp[-1] + b * e[i][1])

print(res if res < inf else -1)
