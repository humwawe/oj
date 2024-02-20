from collections import Counter
from typing import List


class Solution:
  def mostFrequentPrime(self, mat: List[List[int]]) -> int:
    n, m = len(mat), len(mat[0])
    cnt = Counter()

    def f(v):
      s = 2
      while s * s <= v:
        if v % s == 0:
          return False
        s += 1
      return True

    for i in range(n):
      for j in range(m):
        for f_x in range(-1, 2):
          for f_y in range(-1, 2):
            if f_x == 0 and f_y == 0:
              continue
            cur = mat[i][j]
            x, y = i, j
            nx, ny = x + f_x, y + f_y
            while 0 <= nx < n and 0 <= ny < m:
              cur = cur * 10 + mat[nx][ny]
              nx, ny = nx + f_x, ny + f_y
              if f(cur):
                cnt[cur] += 1

    if len(cnt) == 0:
      return -1

    return list(sorted(cnt.items(), key=(lambda x: (-x[1], -x[0]))))[0][0]


s = Solution()
print(s.mostFrequentPrime(mat=[[1, 1], [9, 9], [1, 1]]))
