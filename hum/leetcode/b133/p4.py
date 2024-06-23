from typing import List


class Solution:
  def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
    req = [-1] * n
    for a, b in requirements:
      req[a] = b
    m = max(req)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 1
    mod = 10 ** 9 + 7

    for i in range(n):
      for j in range(m + 1):
        for k in range(i + 1):
          if j + k <= m:
            dp[i + 1][j + k] += dp[i][j]
            dp[i + 1][j + k] %= mod
      if req[i] != -1:
        for j in range(m + 1):
          if req[i] != j:
            dp[i + 1][j] = 0

    return dp[n][req[-1]]
