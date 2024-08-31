from functools import cmp_to_key
from typing import List


class Solution:
  def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
    n = len(damage)
    cnt = [(health[i] + power - 1) // power for i in range(n)]

    def f(i, j):
      return damage[i] * cnt[j] - damage[j] * cnt[i]

    idx = sorted(range(n), key=cmp_to_key(f), reverse=True)

    acc = sum(damage)
    res = 0
    for ii in range(n):
      i = idx[ii]
      res += acc * cnt[i]
      acc -= damage[i]

    return res
