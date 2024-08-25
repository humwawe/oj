from collections import defaultdict
from typing import List


class Solution:
  def countPairs(self, nums: List[int]) -> int:
    res = 0
    nums.sort()
    cnt = defaultdict(int)
    for num in nums:
      st = {num}
      s = list(str(num))
      m = len(s)
      for i in range(m):
        for j in range(i + 1, m):
          s[i], s[j] = s[j], s[i]
          st.add(int(''.join(s)))
          for p in range(i + 1, m):
            for q in range(p + 1, m):
              s[p], s[q] = s[q], s[p]
              st.add(int(''.join(s)))
              s[q], s[p] = s[p], s[q]
          s[j], s[i] = s[i], s[j]
      res += sum(cnt[x] for x in st)
      cnt[num] += 1
    return res
