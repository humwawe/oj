from collections import Counter
from typing import List


class Solution:
  def countCompleteDayPairs(self, hours: List[int]) -> int:
    res = 0
    n = len(hours)
    cnt = Counter()
    for i in range(n):
      res += cnt[(24 - hours[i]) % 24]
      cnt[hours[i] % 24] += 1
    return res
