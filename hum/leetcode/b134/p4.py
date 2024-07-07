from collections import Counter
from typing import List


class Solution:
  def countSubarrays(self, nums: List[int], k: int) -> int:
    cnt = Counter()
    res = 0
    for x in nums:
      ncnt = Counter()
      for c, v in cnt.items():
        if c & x < k:
          continue
        ncnt[c & x] += v
      ncnt[x] += 1
      cnt = ncnt
      res += cnt[k]

    return res
