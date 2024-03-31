from typing import List


class Solution:
  def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
    n = len(nums)

    cnt = [0] * 31
    res = n + 1
    cur = 0
    r = 0
    for i in range(n):
      while r < n and cur < k:
        cur |= nums[r]
        for j in range(31):
          if nums[r] >> j & 1:
            cnt[j] += 1
        r += 1
      if cur < k:
        break
      res = min(res, r - i)
      for j in range(31):
        if nums[i] >> j & 1:
          cnt[j] -= 1
          if cnt[j] == 0:
            cur ^= 1 << j

    return -1 if res == n + 1 else res
