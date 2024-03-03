from typing import List


class Solution:
  def resultArray(self, nums: List[int]) -> List[int]:
    a1, a2 = [nums[0]], [nums[1]]
    n = len(nums)
    for x in nums[2:]:
      if a1[-1] > a2[-1]:
        a1.append(x)
      else:
        a2.append(x)
    return a1 + a2
