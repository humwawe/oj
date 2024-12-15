from collections import Counter
from typing import List


class Solution:
  def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]],
                rates2: List[float]) -> float:
    cur = Counter()
    cur[initialCurrency] = 1

    while True:
      cur1 = Counter(cur)
      for i, (x, y) in enumerate(pairs1):
        for k in cur:
          if x == k:
            cur1[y] = max(cur1[y], cur[x] * rates1[i])
          if y == k:
            cur1[x] = max(cur1[x], cur[y] / rates1[i])

      if cur1 == cur:
        break
      cur = cur1

    while True:
      cur1 = Counter(cur)
      for i, (x, y) in enumerate(pairs2):
        for k in cur:
          if x == k:
            cur1[y] = max(cur1[y], cur[x] * rates2[i])
          if y == k:
            cur1[x] = max(cur1[x], cur[y] / rates2[i])
      if cur1 == cur:
        break
      cur = cur1

    return cur[initialCurrency]


s = Solution()
print(s.maxAmount(initialCurrency="EUR", pairs1=[["EUR", "USD"], ["USD", "JPY"]], rates1=[2.0, 3.0],
                  pairs2=[["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]], rates2=[4.0, 5.0, 6.0]))
