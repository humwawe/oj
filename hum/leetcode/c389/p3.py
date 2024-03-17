from collections import Counter


class Solution:
  def minimumDeletions(self, word: str, k: int) -> int:
    cnt = Counter(word)
    m = len(word)
    tmp = list((cnt[c], c) for c in cnt)
    tmp.sort()
    n = len(tmp)
    res = len(word)
    for i in range(n):
      s = 0
      for j in range(n):
        if j < i:
          s += tmp[j][0]
        else:
          s += max(0, tmp[j][0] - tmp[i][0] - k)
      res = min(res, s)

    return res
