from collections import Counter
from typing import List


class Solution:
  def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
    cnt = [Counter() for _ in range(n)]
    for x, y in pick:
      cnt[x][y] += 1

    res = 0

    for i in range(n):
      if len(cnt[i].values()) > 0 and (max(cnt[i].values())) > i:
        res += 1

    return res
