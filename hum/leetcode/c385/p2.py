from typing import List


class Solution:
  def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    s = set()
    for x in arr2:
      tmp = str(x)
      for i in range(len(tmp)):
        s.add(tmp[:i + 1])
    res = 0
    for x in arr1:
      tmp = str(x)
      for i in range(res, len(tmp)):
        if tmp[:i + 1] in s:
          res = max(res, i + 1)

    return res
