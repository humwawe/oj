from typing import List


class Solution:
  def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
    x, y = 0, 0
    for s in commands:
      if s[0] == 'R':
        y += 1
      elif s[0] == 'U':
        x -= 1
      elif s[0] == 'D':
        x += 1
      else:
        y -= 1
    return x * n + y
