mod = 1_000_000_007
m = 1001

s = [[0] * m for _ in range(m)]
s[0][0] = 1
for i in range(1, m):
  for j in range(1, i + 1):
    s[i][j] = (s[i - 1][j - 1] + j * s[i - 1][j]) % mod


class Solution:
  def numberOfWays(self, n: int, x: int, y: int) -> int:
    res = 0
    perm = pow_y = 1
    for i in range(1, min(n, x) + 1):
      perm = perm * (x + 1 - i) % mod
      pow_y = pow_y * y % mod
      res += perm * s[n][i] * pow_y
    return res % mod
