from collections import defaultdict
from typing import List


class Solution:
  def numberOfSubarrays(self, nums: List[int]) -> int:
    stack = []
    cnt = defaultdict(int)
    res = 0
    for num in nums:
      while stack and num > stack[-1]:
        cnt[stack.pop()] -= 1
      stack.append(num)
      cnt[num] += 1
      res += cnt[num]
    return res
