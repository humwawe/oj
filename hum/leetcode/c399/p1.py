from typing import List


class Solution:
  def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
    res = 0
    n, m = len(nums1), len(nums2)
    for i in range(n):
      for j in range(m):
        if nums1[i] % (nums2[j] * k) == 0:
          res += 1
    return res
