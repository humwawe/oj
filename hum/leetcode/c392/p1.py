from typing import List


class Solution:
  def longestMonotonicSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    res = 0
    for i in range(n):
      for j in range(i, n):
        if (len(set(nums[i:j + 1])) == j - i + 1 and (sorted(nums[i:j + 1]) == nums[i:j + 1]
                                                      or sorted(nums[i:j + 1], reverse=True) == nums[i:j + 1])):
          res = max(res, j - i + 1)
    return res
