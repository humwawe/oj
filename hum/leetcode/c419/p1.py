from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:
  def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    cnt = defaultdict(int)
    L = SortedList()
    R = SortedList()
    sum_l = 0  # L 的元素和

    def add(val: int) -> None:
      if cnt[val] == 0:
        return
      p = (cnt[val], val)
      if L and p > L[0]:
        nonlocal sum_l
        sum_l += p[0] * p[1]
        L.add(p)
      else:
        R.add(p)

    def remove(val: int) -> None:
      if cnt[val] == 0:
        return
      p = (cnt[val], val)
      if p in L:
        nonlocal sum_l
        sum_l -= p[0] * p[1]
        L.remove(p)
      else:
        R.remove(p)

    def l2r() -> None:
      nonlocal sum_l
      p = L[0]
      sum_l -= p[0] * p[1]
      L.remove(p)
      R.add(p)

    def r2l() -> None:
      nonlocal sum_l
      p = R[-1]
      sum_l += p[0] * p[1]
      R.remove(p)
      L.add(p)

    res = [0] * (len(nums) - k + 1)
    for r, in_ in enumerate(nums):
      remove(in_)
      cnt[in_] += 1
      add(in_)

      l = r + 1 - k
      if l < 0:
        continue

      while R and len(L) < x:
        r2l()
      while len(L) > x:
        l2r()
      res[l] = sum_l

      out = nums[l]
      remove(out)
      cnt[out] -= 1
      add(out)
    return res
