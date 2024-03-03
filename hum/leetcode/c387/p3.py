from collections import Counter
from typing import List


class Solution:
  def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
    n = len(grid)
    y_sum = n // 2 * 3 + 1
    o_sum = n * n - y_sum

    cnt1, cnt2 = Counter(), Counter()
    for i in range(n):
      for j in range(n):
        cnt2[grid[i][j]] += 1

    for i in range(n // 2):
      cnt1[grid[i][i]] += 1
      cnt1[grid[i][n - 1 - i]] += 1
    cnt1[grid[n // 2][n // 2]] += 1
    for i in range(n // 2 + 1, n):
      cnt1[grid[i][n // 2]] += 1

    cnt2 -= cnt1

    res = float('inf')
    for i in range(3):
      for j in range(3):
        if i == j:
          continue
        res = min(res, y_sum - cnt1[i] + o_sum - cnt2[j])
    return res
