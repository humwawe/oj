from collections import Counter


class Solution:
  def minAnagramLength(self, s: str) -> int:
    n = len(s)
    res = n
    i = 1

    def f(i):
      cnt = Counter(s[0:i])
      for j in range(0, n, i):
        tmp = Counter(s[j:j + i])
        if cnt != tmp:
          break
      else:
        return i
      return n

    while i * i <= n:
      if n % i == 0:
        res = min(res, f(i))
        res = min(res, f(n // i))
      i += 1
    return res
