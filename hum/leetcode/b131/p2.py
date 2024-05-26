from typing import List


class Solution:
  def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
    t = []
    for i, v in enumerate(nums):
      if v == x:
        t.append(i)

    res = [-1] * len(queries)

    for i, v in enumerate(queries):
      if v <= len(t):
        res[i] = t[v - 1]
    return res
