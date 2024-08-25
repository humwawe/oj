from heapq import heapify, heapreplace, heappop
from typing import List


class Solution:
  def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    if multiplier == 1:
      return nums

    n = len(nums)
    m = max(nums)
    mod = 10 ** 9 + 7

    hpq = [(nums[i], i) for i in range(n)]
    heapify(hpq)
    while k:
      u, i = hpq[0]
      if u == m:
        break
      k -= 1
      heapreplace(hpq, (u * multiplier, i))

    for i in range(n):
      u, j = heappop(hpq)
      nums[j] = u * pow(multiplier, k // n + (i < k % n), mod) % mod

    return nums
