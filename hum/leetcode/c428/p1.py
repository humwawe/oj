from collections import Counter
from typing import List


class Solution:
  def buttonWithLongestTime(self, events: List[List[int]]) -> int:
    last = 0
    cnt = Counter()
    for i, t in events:
      cnt[i] = max(cnt[i], t - last)
      last = t
    res = 0
    for k in sorted(cnt):
      if cnt[k] > cnt[res]:
        res = k
    return res
