from typing import List


class Solution:
  def minimumLevels(self, possible: List[int]) -> int:
    s = 0
    for i in possible:
      if i == 0:
        s -= 1
      else:
        s += 1

    n = len(possible)
    cur = 0
    for i in range(n - 1):
      if possible[i] == 0:
        cur -= 1
      else:
        cur += 1
      if cur > s - cur:
        return i + 1
    return -1
