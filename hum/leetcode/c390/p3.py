import heapq
from typing import List


class Solution:
  def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
    n = len(freq)
    res = []
    cnt = [0] * (10 ** 5 + 5)
    h = []
    for i in range(n):
      cnt[nums[i]] += freq[i]
      heapq.heappush(h, (-cnt[nums[i]], nums[i]))
      while True:
        c, id = h[0]
        if cnt[id] == -c:
          res.append(-c)
          break
        else:
          heapq.heappop(h)

    return res
