class Solution:
  def canAliceWin(self, n: int) -> bool:
    f = 1
    cur = 10
    while n >= cur:
      n -= cur
      f = 1 - f
      cur -= 1

    if f:
      return False
    return True
