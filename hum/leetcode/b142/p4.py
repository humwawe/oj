from itertools import accumulate


class Solution:
  def possibleStringCount(self, word: str, k: int) -> int:
    t = []
    c = 1
    n = len(word)
    res = 1
    mod = 10 ** 9 + 7
    for i in range(1, n):
      if word[i] == word[i - 1]:
        c += 1
      else:
        t.append(c)
        res = (res * c) % mod
        c = 1
    t.append(c)
    res = (res * c) % mod

    mi = len(t)

    t = [x - 1 for x in t if x > 1]
    k -= mi + 1
    if k < 0:
      return res
    nn = len(t)

    dp = [[0] * (k + 1) for _ in range(nn + 1)]
    dp[0][0] = 1
    acc = list(accumulate(dp[0], initial=0))

    for i in range(1, nn + 1):
      for j in range(k + 1):
        dp[i][j] = acc[j + 1] - acc[max(0, j - t[i - 1])]
      acc = list(accumulate(dp[i], initial=0))

    res = (res - acc[-1]) % mod

    return res
