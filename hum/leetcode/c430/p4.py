from math import comb


class Solution:
  def countGoodArrays(self, n: int, m: int, k: int) -> int:
    mod = 1_000_000_007
    return comb(n - 1, k) % mod * m * pow(m - 1, n - k - 1, mod) % mod
