from collections import Counter
from math import inf


class Solution:
  def minimumSubstringsInPartition(self, s: str) -> int:
    n = len(s)
    a = [[0] * n for i in range(n)]
    for i in range(n):
      cnt = Counter()
      f = Counter()
      ma = 0
      for j in range(i, n):
        f[cnt[s[j]]] -= 1
        cnt[s[j]] += 1
        f[cnt[s[j]]] += 1
        ma = max(ma, cnt[s[j]])
        if ma * f[ma] == j - i + 1:
          a[i][j] = 1

    dp = [inf] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
      for j in range(1, i + 1):
        if a[j - 1][i - 1]:
          dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[-1]
