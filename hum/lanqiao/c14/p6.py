n = int(input())
s = input()

dp = [[0] * n for _ in range(n)]
acc = [0] * (n + 1)

for i in range(n):
  acc[i + 1] = acc[i]
  if s[i] != '0':
    acc[i + 1] += 1

res = 0
for i in range(1, n):
  for l in range(n - i):
    r = l + i
    if s[l] == s[r]:
      x = dp[l + 1][r - 1] + 1
      dp[l][r] = x

      if s[l] != '0':
        res += acc[l + x] - acc[l]

print(res)
