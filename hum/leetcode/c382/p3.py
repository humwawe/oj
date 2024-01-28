class Solution:
  def flowerGame(self, n: int, m: int) -> int:
    res = 0
    for i in range(1, n + 1):
      if i % 2 == 1:
        res += m // 2
      else:
        res += m - m // 2

    return res
