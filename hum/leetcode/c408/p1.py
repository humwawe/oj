from typing import List


class Solution:
  def canAliceWin(self, nums: List[int]) -> bool:
    s = sum(nums)
    x = sum([num for num in nums if num < 10])
    y = sum([num for num in nums if 10 <= num <= 99])
    if x > s - x or y > s - y:
      return True
    return False
