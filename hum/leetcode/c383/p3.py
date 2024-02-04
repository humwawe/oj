from typing import List


class Solution:
  def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
    n, m = len(image), len(image[0])
    cum = [[0] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]

    def helper(i, j):
      if i + 2 >= n or j + 2 >= m:
        return -1
      for k in range(3):
        for l in range(2):
          if abs(image[i + k][j + l] - image[i + k][j + l + 1]) > threshold:
            return -1
      for k in range(3):
        for l in range(2):
          if abs(image[i + l][j + k] - image[i + l + 1][j + k]) > threshold:
            return -1

      cur = 0
      for k in range(3):
        for l in range(3):
          cur += image[i + k][j + l]
      return cur // 9

    for i in range(n):
      for j in range(m):
        t = helper(i, j)
        if t != -1:
          for k in range(3):
            for l in range(3):
              cum[i + k][j + l] += t
              cnt[i + k][j + l] += 1
    res = [[0] * m for _ in range(n)]
    for i in range(n):
      for j in range(m):
        if cnt[i][j] == 0:
          res[i][j] = image[i][j]
        else:
          res[i][j] = cum[i][j] // cnt[i][j]

    return res
