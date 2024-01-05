l = int(input())
s, t, _ = map(int, input().split())
a = list(map(int, input().split()))

if s == t:
  res = 0
  for i in a:
    if i % s == 0:
      res += 1
  print(res)
  exit(0)

a.append(0)
a.append(l)
a.sort()
N = 100
w = [0]
for i in range(1, len(a)):
  w.extend([0] * min(a[i] - a[i - 1] - 1, N))
  w.append(1)

w[-1] = 0
w.extend([0] * N)
m = len(w)

dp = [10 ** 15] * m
dp[0] = 0
for i in range(1, m):
  for j in range(s, t + 1):
    if i - j >= 0:
      dp[i] = min(dp[i], dp[i - j] + w[i])

print(min(dp[-N - 1:]))
