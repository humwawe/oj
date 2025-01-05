from collections import defaultdict
from typing import List


class Solution:
  def numberOfSubsequences(self, nums: List[int]) -> int:
    ans = 0
    cnt = defaultdict(int)
    for i in range(4, len(nums) - 2):
      b = nums[i - 2]
      for a in nums[:i - 3]:
        cnt[a / b] += 1
      c = nums[i]
      for d in nums[i + 2:]:
        ans += cnt[d / c]
    return ans
