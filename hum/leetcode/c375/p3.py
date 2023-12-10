from typing import List


class Solution:
  def countSubarrays(self, nums: List[int], k: int) -> int:
    v = max(nums)
    n = len(nums)
    cnt = 0
    res = 0
    j = -1

    def check(x):
      return 1 if v == x else 0

    for i in range(n):
      if nums[i] == v:
        cnt += 1
      if cnt >= k:
        while j + 1 < n and cnt - check(nums[j + 1]) >= k:
          cnt -= check(nums[j + 1])
          j += 1

        res += j + 2
    return res
