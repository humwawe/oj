from collections import Counter
from typing import List


class Solution:
  def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
    cnt1 = Counter([x for x in nums1 if x % k == 0])
    nums2 = [x * k for x in nums2]
    cnt2 = Counter(nums2)

    res = 0

    for x, y in cnt1.items():
      i = 1
      while i * i <= x:
        if x % i == 0:
          res += y * cnt2[i]
          if i * i != x:
            res += y * cnt2[x // i]
        i += 1
    return res
