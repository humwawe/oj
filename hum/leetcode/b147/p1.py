class Solution:
  def hasMatch(self, s: str, p: str) -> bool:
    t = p.split('*')
    if len(t) == 1:
      return t[0] in s
    else:
      i = s.find(t[0])
      j = s.rfind(t[1])
      if i == -1 or j == -1:
        return False
      return i + len(t[0]) <= j
