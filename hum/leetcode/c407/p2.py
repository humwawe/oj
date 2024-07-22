class Solution:
  def doesAliceWin(self, s: str) -> bool:
    res = 0
    res += s.count('a')
    res += s.count('e')
    res += s.count('i')
    res += s.count('o')
    res += s.count('u')
    if res == 0:
      return False

    return True
