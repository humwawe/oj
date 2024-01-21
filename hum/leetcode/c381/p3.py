from collections import Counter


class Solution:
  def minimumPushes(self, word: str) -> int:
    cnt = Counter(word)
    cur = 1
    res = 0
    for val in sorted(cnt.values(), reverse=True):
      res += val * ((cur + 7) // 8)
      cur += 1
    return res
