from typing import List


class Solution:
  def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
    n, m = len(nums), len(changeIndices)
    inf = float('inf')
    res = inf

    def f(tmp):
      if len(tmp) < n:
        return False
      s = 0
      for v in tmp:
        c = changeIndices[v]
        if nums[c - 1] > v - s:
          return False
        s += nums[c - 1]
        s += 1
      return True

    for i in range(m - 1, -1, -1):
      s = set()
      tmp = []
      for j in range(i, -1, -1):
        if changeIndices[j] not in s:
          tmp.append(j)
          s.add(changeIndices[j])
      tmp.reverse()
      if f(tmp):
        res = min(res, i + 1)
    return res if res != inf else -1
