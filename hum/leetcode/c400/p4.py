from typing import List


class Solution:
  def minimumDifference(self, nums: List[int], k: int) -> int:
    n = len(nums)
    s = set()
    res = float('inf')
    for i in range(n):
      ns = set()
      ns.add(nums[i])
      for e in s:
        ns.add(e & nums[i])
      for e in ns:
        res = min(res, abs(e - k))
      s = ns
    return res
