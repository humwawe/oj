from typing import List


class Solution:
  def constructTransformedArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = []
    for i in range(n):
      res.append(nums[(i + nums[i]) % n])
    return res
