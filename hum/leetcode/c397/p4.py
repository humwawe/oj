from collections import defaultdict
from math import inf
from typing import List


class Solution:
  def findPermutation(self, nums: List[int]) -> List[int]:
    n = len(nums)
    lim = 1 << n
    d = defaultdict(lambda: (inf, [inf]))
    d[(1, 0)] = (0, [0])

    for _ in range(n - 1):
      nd = defaultdict(lambda: (inf, [inf]))
      for st, e in d:
        f = (n - st.bit_count()) >= 2
        for i in range(n):
          if st >> i & 1 == 0:
            nst = (st | (1 << i), i)
            v, l = d[(st, e)]
            nl = l[:]
            nl.append(i)
            nv = v + abs(e - nums[i])
            if not f:
              nv += abs(i - nums[0])

            if nv < nd[nst][0]:
              nd[nst] = (nv, nl)
            elif nv == nd[nst][0] and nl < nd[nst][1]:
              nd[nst] = (nv, nl)
      d = nd

    st = (inf, [inf])
    for i in range(n):
      if d[(lim - 1, i)][0] < st[0]:
        st = d[(lim - 1, i)]
      elif d[(lim - 1, i)][0] == st[0] and d[(lim - 1, i)][1] < st[1]:
        st = d[(lim - 1, i)]

    return st[1]


s = Solution()
print(s.findPermutation([0, 3, 2, 1]))
