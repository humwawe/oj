from typing import List


class Solution:
  def minimumAddedCoins(self, coins: List[int], target: int) -> int:
    coins.sort()
    s = 0
    i = 0
    res = 0
    while s < target:
      if i < len(coins) and coins[i] <= s + 1:
        s += coins[i]
        i += 1
        continue
      else:
        s += s + 1
        res += 1
    return res


s = Solution()
print(s.minimumAddedCoins([1, 4, 10], 19))
