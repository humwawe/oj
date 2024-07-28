class PrimeTable:
  def __init__(self, n: int) -> None:
    self.N = n
    self.pr = []
    # 存最大质因子
    self.max_div = list(range(n + 1))
    # self.phi = list(range(n + 1))

    for i in range(2, n + 1):
      if self.max_div[i] == i:
        self.pr.append(i)
        for j in range(i, n + 1, i):
          self.max_div[j] = i
        #  self.phi[j] = self.phi[j] // i * (i - 1)

  def is_prime(self, x: int):
    if x < 2:
      return False
    if x <= self.N:
      return self.max_div[x] == x
    for p in self.pr:
      if p * p > x:
        break
      if x % p == 0:
        return False
    return True


pr = PrimeTable(10 ** 5)


class Solution:
  def nonSpecialCount(self, l: int, r: int) -> int:

    res = 0
    for i in range(1, 10 ** 5):
      if l <= i * i <= r and pr.is_prime(i):
        res += 1
      if i * i > r:
        break
    return r - l + 1 - res
