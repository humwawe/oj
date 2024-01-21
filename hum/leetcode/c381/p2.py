from typing import List


class Solution:
  def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
    x -= 1
    y -= 1
    res = [0] * n
    for i in range(n):
      for j in range(i):
        res[min(i - j, abs(x - i) + 1 + abs(y - j), abs(i - y) + 1 + abs(j - x)) - 1] += 2
    return res
