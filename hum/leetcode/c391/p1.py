class Solution:
  def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
    t = x
    s = 0
    while t:
      s += t % 10
      t //= 10
    if x % s == 0:
      return s
    return -1
