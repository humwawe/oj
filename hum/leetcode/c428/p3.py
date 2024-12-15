from typing import List

MOD = 10 ** 18 + 3
base = 131
MX = 5000
f = [1] * (MX + 1)
for i in range(1, MX + 1):
  f[i] = f[i - 1] * base % MOD


class Solution:
  def beautifulSplits(self, nums: List[int]) -> int:
    n = len(nums)
    hval = [0] * (n + 1)
    for i, x in enumerate(nums):
      hval[i + 1] = (hval[i] * base + x + 1) % MOD

    def substr(i: int, l: int):
      return (hval[i + l] - hval[i] * f[l]) % MOD

    res = 0
    for i in range(1, n - 1):
      l1 = i
      s1 = substr(0, l1)
      for j in range(i + 1, n):
        l2 = j - i
        if l1 <= l2 and s1 == substr(i, l1):
          res += n - j
          break
        s2 = substr(i, l2)
        l3 = n - j
        if l2 <= l3 and s2 == substr(j, l2):
          res += 1
    return res
