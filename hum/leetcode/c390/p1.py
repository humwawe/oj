from collections import Counter


class Solution:
  def maximumLengthSubstring(self, s: str) -> int:
    n = len(s)
    res = 0

    def check(tmp):
      cnt = Counter(tmp)
      return max(cnt.values()) <= 2

    for i in range(n):
      for j in range(i + 1, n):
        if check(s[i:j + 1]):
          res = max(res, j - i + 1)

    return res
