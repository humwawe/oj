from collections import Counter


class Solution:
  def minimumLength(self, s: str) -> int:
    cnt = Counter(s)
    res = 0
    for value in cnt.values():
      if value % 2 == 0:
        res += 2
      else:
        res += 1
    return res
