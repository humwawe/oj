from itertools import pairwise
from typing import List


class Factorial:
  def __init__(self, n, mod) -> None:
    n += 5
    self.mod = mod
    self.f = [1 for _ in range(n)]
    self.g = [1 for _ in range(n)]

    for i in range(1, n):
      self.f[i] = self.f[i - 1] * i % self.mod

    # self.g[-1] = pow(self.f[-1], mod - 2, mod)
    self.g[-1] = pow(self.f[-1], -1, mod)

    for i in range(n - 2, -1, -1):
      self.g[i] = self.g[i + 1] * (i + 1) % self.mod

  def fac(self, n):
    return self.f[n]

  def fac_inv(self, n):
    return self.g[n]

  def comb(self, n, m):
    if n < m or m < 0 or n < 0: return 0
    return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

  def perm(self, n, m):
    if n < m or m < 0 or n < 0: return 0
    return self.f[n] * self.g[n - m] % self.mod

  def catalan(self, n):
    return (self.comb(2 * n, n) - self.comb(2 * n, n - 1)) % self.mod

  def inv(self, n):
    return self.f[n - 1] * self.g[n] % self.mod


mod = 10 ** 9 + 7
fact = Factorial(int(1e5) + 5, mod)


class Solution:
  def numberOfSequence(self, n: int, sick: List[int]) -> int:
    m = len(sick)
    l = n - m
    res = fact.comb(l, sick[0]) * fact.comb(l - sick[0], n - sick[-1] - 1) % mod
    l -= sick[0] + n - sick[-1] - 1
    s = 0
    for x, y in pairwise(sick):
      ll = y - x - 1
      if ll:
        s += ll - 1
        res = res * fact.comb(l, ll) % mod
        l -= ll
    res = res * pow(2, s, mod) % mod
    return res
