from collections import Counter

mod = 10 ** 9 + 7
M = 80
fac = [0] * (M + 1)
fac[1] = 1
inv_fac = [0] * (M + 1)
inv_fac[1] = 1
for i in range(2, M + 1):
  fac[i] = i * fac[i - 1] % mod
  inv_fac[i] = inv_fac[i - 1] * pow(i, mod - 2, mod) % mod


class Solution:
  def countBalancedPermutations(self, num: str) -> int:
    num = [int(i) for i in num]

    s = sum(num)
    if s % 2 != 0:
      return 0
    n = len(num)
    m = s // 2
    c = n // 2
    dp = [[0] * (m + 1) for _ in range(c + 1)]
    dp[0][0] = 1
    for i in range(n):
      ndp = [[0] * (m + 1) for _ in range(c + 1)]
      for pre_c in range(c + 1):
        for pre_v in range(m + 1):
          ndp[pre_c][pre_v] = (ndp[pre_c][pre_v] + dp[pre_c][pre_v]) % mod
          nc = pre_c + 1
          if nc > c:
            continue
          nv = pre_v + num[i]
          if nv > m:
            continue
          ndp[nc][nv] = (ndp[nc][nv] + dp[pre_c][pre_v]) % mod
      dp = ndp

    res = dp[c][m] * fac[c] * fac[n - c] % mod

    cnt = Counter(num)
    for x in cnt.values():
      res = res * inv_fac[x] % mod
    return res
