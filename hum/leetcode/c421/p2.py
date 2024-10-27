from collections import Counter


class Solution:
  def lengthAfterTransformations(self, s: str, t: int) -> int:
    s = [ord(c) - ord('a') for c in s]
    cnt = Counter(s)
    res = len(s)
    mod = 10 ** 9 + 7
    for i in range(t):
      res = (res + cnt[25]) % mod
      ncnt = Counter()
      for i in range(25):
        ncnt[i + 1] = cnt[i]
      ncnt[0] += cnt[25]
      ncnt[1] += cnt[25]
      cnt = ncnt

    return res
