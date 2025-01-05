from typing import List


class Solution:
  def maximumCoins(self, coins: List[List[int]], k: int) -> int:
    n = len(coins)
    coins.sort()
    ls, rs = [], []

    acc = [0]
    for l, r, c in coins:
      ls.append(l)
      rs.append(r)
      acc.append(acc[-1] + c * (r - l + 1))

    j = -1
    res = 0
    for i in range(n):
      while j + 1 < n and ls[j + 1] - ls[i] <= k:
        j += 1
      last = (min(ls[i] + k - 1, rs[j]) - ls[j] + 1) * coins[j][2]
      t = acc[j] - acc[i] + last
      res = max(res, t)

    j = n - 1
    for i in range(n - 1, -1, -1):
      while j - 1 >= 0 and rs[i] - rs[j - 1] <= k:
        j -= 1
      last = (rs[j] - max(rs[i] - k + 1, ls[j]) + 1) * coins[j][2]
      t = acc[i + 1] - acc[j + 1] + last
      res = max(res, t)

    return res


s = Solution()
print(s.maximumCoins(coins=[[8, 10, 1], [1, 3, 2], [5, 6, 4]], k=4))
