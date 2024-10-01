from typing import List


class Solution:
  def validSequence(self, word1: str, word2: str) -> List[int]:
    n, m = len(word1), len(word2)

    def f(s, t):
      dp = [0] * n
      j = 0
      if s[0] == t[j]:
        dp[0] = 1
        j += 1
      for i in range(1, n):
        if j < m and s[i] == t[j]:
          dp[i] = dp[i - 1] + 1
          j += 1
        else:
          dp[i] = dp[i - 1]

      return dp

    pre = f(word1, word2)
    suf = f(word1[::-1], word2[::-1])[::-1]
    s, j = 0, 0
    while s < n and j < m and word1[s] == word2[j]:
      s += 1
      j += 1

    t = -1
    for i in range(s, n):
      cur = 0
      if i > 0:
        cur += pre[i - 1]
      if i + 1 < n:
        cur += suf[i + 1]
      if cur + 1 >= m:
        t = i
        break

    if j != m and t == -1:
      return []

    j = 0
    res = []
    for i in range(n):
      if j == m:
        return res

      if i != t:
        if word1[i] == word2[j]:
          res.append(i)
          j += 1
      else:
        res.append(i)
        j += 1
    return res


s = Solution()
print(s.validSequence("ab", "ab"))
