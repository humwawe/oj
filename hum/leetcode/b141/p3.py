from math import inf
from typing import List


class Solution:
  def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
    n, m = len(source), len(pattern)
    dp = [[-inf] * (m + 1) for _ in range(n + 1)]

    sorce = [0] * n
    for i in targetIndices:
      sorce[i] = 1

    dp[0][0] = 0

    for i in range(1, n + 1):
      dp[i][0] = dp[i - 1][0] + sorce[i - 1]

    print(dp)

    for i in range(1, n + 1):
      for j in range(1, m + 1):
        if source[i - 1] == pattern[j - 1]:
          dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
          dp[i][j] = max(dp[i][j], dp[i - 1][j] + sorce[i - 1])
        else:
          dp[i][j] = dp[i - 1][j] + sorce[i - 1]

    print(dp)
    return dp[n][m]


s = Solution()
print(s.maxRemovals("ada", "d", [0, 2]))
