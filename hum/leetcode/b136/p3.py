from typing import List


class Solution:
  def minFlips(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    res = 0
    for i in range(n // 2):
      for j in range(m // 2):
        t = grid[i][j] + grid[i][-1 - j] + grid[-1 - i][j] + grid[-1 - i][-1 - j]
        res += min(t, 4 - t)

    cnt1, cnt2 = 0, 0
    if n % 2 == 1:
      r = n // 2
      for j in range(m // 2):
        if grid[r][j] != grid[r][-1 - j]:
          res += 1
          cnt1 += 1
        else:
          if grid[r][j] == 1:
            cnt2 += 1

    if m % 2 == 1:
      c = m // 2
      for i in range(n // 2):
        if grid[i][c] != grid[-1 - i][c]:
          res += 1
          cnt1 += 1
        else:
          if grid[i][c] == 1:
            cnt2 += 1

    if n % 2 and m % 2:
      res += grid[n // 2][m // 2]

    if cnt1 == 0 and cnt2 % 2 != 0:
      res += 2

    return res


s = Solution()
print(s.minFlips([[1], [1], [0], [1], [1]]))
