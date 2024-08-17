n = int(input())
powers = []
for i in range(2, 10 ** 6):
  cnt = 0
  while n % i == 0:
    n //= i
    cnt += 1
  if cnt >= 2:
    powers.append(cnt)

if n > 1 and round(n ** 0.5) ** 2 == n:
  powers.append(2)

m = 60
dp = [[0] * m for _ in range(m)]
dp[0][0] = 1

for _ in range(m):
  ndp = [[0] * m for _ in range(m)]
  for i in range(m):
    for j in range(m):
      for k in range(j, m):
        if i + k < m:
          ndp[i + k][k] += dp[i][j]
  dp = ndp

cnt = [sum(x) for x in dp]

res = 1
for x in powers:
  res *= cnt[x]

print(res - 1)
