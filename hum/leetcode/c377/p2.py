from typing import List


class Solution:
  def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    mod = 10 ** 9 + 7
    hFences.append(1)
    hFences.append(m)
    hFences.sort()
    vFences.append(1)
    vFences.append(n)
    vFences.sort()
    vs = set()
    for i in range(len(vFences)):
      for j in range(i + 1, len(vFences)):
        vs.add(vFences[j] - vFences[i])
    res = -1
    for i in range(len(hFences)):
      for j in range(i + 1, len(hFences)):
        if hFences[j] - hFences[i] in vs:
          res = max(res, (hFences[j] - hFences[i]) * (hFences[j] - hFences[i]))
    if res != -1:
      return res % mod
    return res
