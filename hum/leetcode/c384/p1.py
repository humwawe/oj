from typing import List


class Solution:
  def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    n, m = len(matrix), len(matrix[0])
    res = [[matrix[i][j] for j in range(m)] for i in range(n)]
    tmp = [0] * m
    for i in range(n):
      for j in range(m):
        tmp[j] = max(tmp[j], matrix[i][j])

    for i in range(n):
      for j in range(m):
        if res[i][j] == -1:
          res[i][j] = tmp[j]

    return res
