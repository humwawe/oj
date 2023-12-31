from typing import List


class Solution:
  def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    n = len(s) // 2
    t = s[n:][::-1]
    s = s[:n]

    diff_sum = [0] * (n + 1)
    for i in range(n):
      diff_sum[i + 1] = diff_sum[i] + (1 if s[i] != t[i] else 0)

    s_sum, t_sum = [[0] * 26 for _ in range(n + 1)], [[0] * 26 for _ in range(n + 1)]
    for i in range(n):
      s_sum[i + 1][:] = s_sum[i][:]
      s_sum[i + 1][ord(s[i]) - ord('a')] += 1
      t_sum[i + 1][:] = t_sum[i][:]
      t_sum[i + 1][ord(t[i]) - ord('a')] += 1

    def count(c_sum, l, r):
      return [x - y for x, y in zip(c_sum[r + 1], c_sum[l])]

    def sub(ss1, ss2):
      for i in range(len(ss2)):
        ss1[i] -= ss2[i]
        if ss1[i] < 0:
          return False
      return ss1

    def helper(s_sum, t_sum):
      if diff_sum[a] > 0 or diff_sum[n] - diff_sum[max(b + 1, d + 1)] > 0:
        return False

      if d <= b:
        return count(s_sum, a, b) == count(t_sum, a, b)

      if b < c:
        if diff_sum[c] - diff_sum[b + 1] > 0:
          return False
        return count(s_sum, a, b) == count(t_sum, a, b) and count(s_sum, c, d) == count(t_sum, c, d)

      s1 = sub(count(s_sum, a, b), count(t_sum, a, c - 1))
      s2 = sub(count(t_sum, c, d), count(s_sum, b + 1, d))
      return s1 and s2 and s1 == s2

    res = []
    for a, b, c, d in queries:
      c, d = n * 2 - 1 - d, n * 2 - 1 - c
      if a > c:
        a, b, c, d = c, d, a, b
        res.append(helper(t_sum, s_sum))
      else:
        res.append(helper(s_sum, t_sum))

    return res
