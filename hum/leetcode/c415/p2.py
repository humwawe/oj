from math import inf
from typing import List


class Solution:
  def maxScore(self, a: List[int], b: List[int]) -> int:
    n = len(b)
    dp1 = [-inf] * n
    dp1[0] = a[0] * b[0]
    for i in range(1, n):
      dp1[i] = max(dp1[i - 1], a[0] * b[i])
    dp2 = [-inf] * n
    dp2[1] = dp1[0] + a[1] * b[1]
    for i in range(2, n):
      dp2[i] = max(dp2[i - 1], dp1[i - 1] + a[1] * b[i])

    dp3 = [-inf] * n
    dp3[2] = dp2[1] + a[2] * b[2]
    for i in range(3, n):
      dp3[i] = max(dp3[i - 1], dp2[i - 1] + a[2] * b[i])

    dp4 = [-inf] * n
    dp4[3] = dp3[2] + a[3] * b[3]
    for i in range(4, n):
      dp4[i] = max(dp4[i - 1], dp3[i - 1] + a[3] * b[i])

    return dp4[-1]
