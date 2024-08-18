class Solution:
  def countKConstraintSubstrings(self, s: str, k: int) -> int:
    n = len(s)
    res = 0
    for i in range(n):
      for j in range(i, n):
        z = s[i:j + 1].count("0")
        if z <= k or j - i + 1 - z <= k:
          res += 1
    return res
