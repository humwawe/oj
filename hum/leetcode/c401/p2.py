class Solution:
  def valueAfterKSeconds(self, n: int, k: int) -> int:
    a = [1] * n
    mod = 10 ** 9 + 7
    for i in range(k):
      s = 0
      for j in range(n):
        s += a[j]
        s %= mod
        a[j] = s
    return a[-1] % mod
