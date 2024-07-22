from typing import List


class Solution:
  def minimumOperations(self, nums: List[int], target: List[int]) -> int:
    n = len(nums)
    diff1 = [nums[0]]
    for i in range(1, n):
      diff1.append(nums[i] - nums[i - 1])

    diff2 = [target[0]]
    for i in range(1, n):
      diff2.append(target[i] - target[i - 1])

    res1, res2 = 0, 0
    for i in range(n):
      if diff1[i] > diff2[i]:
        res1 += diff1[i] - diff2[i]
      else:
        res2 += diff2[i] - diff1[i]

    return max(res1, res2)
