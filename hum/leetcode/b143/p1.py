class Solution:
  def smallestNumber(self, n: int, t: int) -> int:
    cur = n
    while True:
      s = 1
      tmp = cur
      while tmp:
        s *= tmp % 10
        tmp //= 10
      if s % t == 0:
        return cur
      cur += 1
