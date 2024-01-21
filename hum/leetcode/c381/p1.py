from collections import Counter


class Solution:
  def minimumPushes(self, word: str) -> int:
    cnt = Counter()
    for c in word:
      cnt[c] += 1
    vals = list(cnt.values())
    cur = 1
    res = 0
    for val in sorted(vals, reverse=True):
      res += val * ((cur + 7) // 8)
      cur += 1
    return res
