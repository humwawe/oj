from typing import List

from sortedcontainers import SortedList


class Solution:
  def resultArray(self, nums: List[int]) -> List[int]:
    a1, a2 = [nums[0]], [nums[1]]
    t1, t2 = SortedList([nums[0]]), SortedList([nums[1]])

    def gc(arr, v):
      return len(arr) - arr.bisect_right(v)

    for x in nums[2:]:
      n1, n2 = gc(t1, x), gc(t2, x)
      if n1 > n2:
        a1.append(x)
        t1.add(x)
      elif n1 < n2:
        a2.append(x)
        t2.add(x)
      else:
        if len(a1) <= len(a2):
          a1.append(x)
          t1.add(x)
        else:
          a2.append(x)
          t2.add(x)
    return a1 + a2
