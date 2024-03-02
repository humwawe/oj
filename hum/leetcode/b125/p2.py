import heapq
from typing import List


class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    res = 0
    while len(nums) >= 2:
      x, y = heapq.heappop(nums), heapq.heappop(nums)
      if x >= k:
        return res
      heapq.heappush(nums, min(x, y) * 2 + max(x, y))
      res += 1

    return res
