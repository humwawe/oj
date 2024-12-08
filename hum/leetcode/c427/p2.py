from typing import List


class Solution:
  def maxRectangleArea(self, points: List[List[int]]) -> int:
    n = len(points)

    def f(a, b, c, d):
      tmp = []
      tmp.append((points[a][0], points[a][1]))
      tmp.append((points[b][0], points[b][1]))
      tmp.append((points[c][0], points[c][1]))
      tmp.append((points[d][0], points[d][1]))
      tmp.sort()
      if len(set(tmp)) != 4: return -1

      if tmp[0][0] != tmp[1][0] or tmp[2][0] != tmp[3][0]:
        return -1

      if tmp[0][1] != tmp[2][1] or tmp[1][1] != tmp[3][1]:
        return -1

      x1, x2 = tmp[0][0], tmp[2][0]
      y1, y2 = tmp[0][1], tmp[1][1]
      for i in range(n):
        if i == a or i == b or i == c or i == d: continue
        if x1 <= points[i][0] <= x2 and y1 <= points[i][1] <= y2:
          return -1
      print(a, b, c, d)
      return (x2 - x1) * (y2 - y1)

    res = -1
    for a in range(n):
      for b in range(n):
        for c in range(n):
          for d in range(n):
            res = max(res, f(a, b, c, d))

    return res
