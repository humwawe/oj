from math import comb

M = 800
dp = [-1] * (M + 1)
dp[1] = 0

for i in range(2, M + 1):
  dp[i] = dp[i.bit_count()] + 1


class Solution:
  def countKReducibleNumbers(self, s: str, k: int) -> int:
    n = len(s)

    res = 0
    mod = 10 ** 9 + 7

    def f(c):
      cnt1 = 0
      res = 0
      for i in range(n):
        if s[i] == '0':
          continue
        if c - cnt1 < 0 or c - cnt1 > n - i - 1:
          return res
        res = (res + comb(n - i - 1, c - cnt1)) % mod
        cnt1 += int(s[i])
      return res

    for c in range(1, n + 1):
      if dp[c] <= k - 1:
        res = (res + f(c)) % mod
    return res
