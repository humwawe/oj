from typing import List


class Solution:
  def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
    n = len(rectangles)
    t = [(rec[1], rec[3]) for rec in rectangles]
    t.sort()
    r_max = 0
    cur = 0
    for i in range(n):
      if t[i][0] >= r_max:
        cur += 1
      r_max = max(r_max, t[i][1])
    if cur >= 3:
      return True

    t = [(rec[0], rec[2]) for rec in rectangles]
    t.sort()
    r_max = 0
    cur = 0
    for i in range(n):
      if t[i][0] >= r_max:
        cur += 1
      r_max = max(r_max, t[i][1])
    if cur >= 3:
      return True
    return False
