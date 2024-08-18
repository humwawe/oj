from math import inf
from typing import List


class Solution:

  def maximumValueSum(self, board: List[List[int]]) -> int:
    fmax = lambda x, y: x if x >= y else y
    n, m = len(board), len(board[0])
    pre_m = [[-inf] * m for _ in range(n)]

    for i in range(n):
      for j in range(m):
        if i == 0:
          pre_m[i][j] = board[i][j]
        pre_m[i][j] = fmax(pre_m[i - 1][j], board[i][j])

    suf_m = [[] for _ in range(n)]

    cur = [-inf] * m
    for i in range(n - 1, -1, -1):
      cur = [fmax(cur[j], board[i][j]) for j in range(m)]
      m1, m2, m3 = -1, -1, -1
      for j in range(m):
        if m1 == -1 or cur[j] >= cur[m1]:
          m1, m2, m3 = j, m1, m2
        elif m2 == -1 or cur[j] >= cur[m2]:
          m2, m3 = j, m2
        elif m3 == -1 or cur[j] > cur[m3]:
          m3 = j
      suf_m[i].append(m1)
      suf_m[i].append(m2)
      suf_m[i].append(m3)
      suf_m[i].append(cur[m1])
      suf_m[i].append(cur[m2])
      suf_m[i].append(cur[m3])

    res = -inf
    for i in range(1, n - 1):
      for j in range(m):
        for k in range(m):
          if j == k:
            continue
          m1, m2, m3 = suf_m[i + 1][0], suf_m[i + 1][1], suf_m[i + 1][2]
          if m1 != j and m1 != k:
            res = fmax(res, board[i][j] + pre_m[i - 1][k] + suf_m[i + 1][3])
          elif m2 != j and m2 != k:
            res = fmax(res, board[i][j] + pre_m[i - 1][k] + suf_m[i + 1][4])
          else:
            res = fmax(res, board[i][j] + pre_m[i - 1][k] + suf_m[i + 1][5])

    return res
