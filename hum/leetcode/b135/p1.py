class Solution:
  def losingPlayer(self, x: int, y: int) -> str:
    f = 0
    while x >= 1 and y >= 4:
      x -= 1
      y -= 4
      f ^= 1
    if f == 1:
      return "Alice"
    else:
      return "Bob"
