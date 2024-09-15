from math import inf
from typing import List


class Solution:
  def minValidStrings(self, words: List[str], target: str) -> int:
    n = len(target)

    def kmp_pre(s):
      n = len(s)
      kmp = [0] * (n + 1)
      kmp[0] = -1
      j = 0
      for i in range(1, n):
        while j >= 0 and s[i] != s[j]:
          j = kmp[j]
        j += 1
        kmp[i + 1] = j
      return kmp

    dp = [inf] * (n + 1)
    dp[0] = 0

    tmp = [0] * n
    for word in words:
      tmp_s = word + "#" + target
      zs = kmp_pre(tmp_s)
      sl = len(word) + 2
      for i in range(sl, len(zs)):
        tmp[i - sl] = max(tmp[i - sl], zs[i])

    for i in range(n):
      dp[i + 1] = min(dp[i + 1], dp[i + 1 - tmp[i]] + 1)

    return -1 if dp[n] == inf else dp[n]
