class Solution:
  def findPermutationDifference(self, s: str, t: str) -> int:
    res = 0
    for i, c in enumerate(s):
      j = t.find(c)
      res += abs(j - i)
    return res
