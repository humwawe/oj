class Solution:
  def isSubstringPresent(self, s: str) -> bool:
    n = len(s)
    for i in range(n - 1):
      tmp = s[i:i + 2]

      if s.find(tmp[::-1]) != -1:
        return True
    return False
