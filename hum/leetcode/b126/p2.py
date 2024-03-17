from typing import List


class Solution:
  def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    s = sum(nums)
    idx = sorted(range(n), key=lambda x: nums[x])
    rem = set()
    res = []
    j = 0
    for i, k in queries:
      if i not in rem:
        s -= nums[i]
        rem.add(i)

      now = j
      cnt = 0
      while now < n and now - j - cnt < k:
        if idx[now] not in rem:
          s -= nums[idx[now]]
          rem.add(idx[now])
        else:
          cnt += 1
        now += 1
      j = now

      res.append(s)
    return res
