from typing import List


class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    n = len(original)
    mat = [[10 ** 12 for _ in range(26)] for _ in range(26)]

    for i in range(n):
      x = ord(original[i]) - ord('a')
      y = ord(changed[i]) - ord('a')
      mat[x][y] = min(mat[x][y], cost[i])

    for i in range(26):
      mat[i][i] = 0
    for k in range(26):
      for i in range(26):
        for j in range(26):
          mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

    n = len(source)
    res = 0
    for i in range(n):
      if source[i] != target[i]:
        res += mat[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
    if res >= 10 ** 12:
      return -1
    return res
