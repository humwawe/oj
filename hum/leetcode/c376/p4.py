from typing import List


class Solution:
  def maxFrequencyScore(self, nums: List[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    s = [0] * (n + 1)

    def check(l, r):
      length = r - l + 1
      tmp = 0
      med = l + length // 2
      x = nums[med]
      tmp += x * (med - l + 1) - (s[med + 1] - s[l])
      tmp += (s[r + 1] - s[med + 1]) - x * (r - med)

      return tmp <= k

    res = 0
    for i in range(n):
      s[i + 1] = s[i] + nums[i]
      l = 0
      r = i
      while l < r:
        mid = l + r >> 1
        if check(mid, i):
          r = mid
        else:
          l = mid + 1
      res = max(res, i - l + 1)

    return res
