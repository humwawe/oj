class Solution:
  def calculateScore(self, s: str) -> int:
    t = [[] for _ in range(26)]
    res = 0
    for i, c in enumerate(s):
      x = 25 - (ord(c) - ord('a'))
      if t[x]:
        res += i - t[x].pop()
      else:
        t[ord(c) - ord('a')].append(i)
    return res
