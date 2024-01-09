from typing import List


class Solution:
  def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    s1 = set(nums1)
    s2 = set(nums2)
    s_common = s1 & s2

    n1 = len(s1)
    n2 = len(s2)
    n_common = len(s_common)

    res = n1 + n2 - n_common

    if n1 > n // 2:
      n1_rem = min(n_common, n1 - n // 2)
      n_common -= n1_rem
      n1 -= n1_rem
      res -= n1 - n // 2

    if n2 > n // 2:
      n2_rem = min(n_common, n2 - n // 2)
      n_common -= n2_rem
      n2 -= n2_rem
      res -= n2 - n // 2

    return res
