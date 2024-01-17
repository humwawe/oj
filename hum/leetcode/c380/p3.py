from functools import cache


class Solution:
  def findMaximumNumber(self, k: int, x: int) -> int:
    l = 0
    r = 10 ** 15

    def dp(s_num):
      n = len(s_num)
      num = list(map(int, str(s_num)))

      @cache
      def __dfs(i, cnt, limit, lead):
        if i == n:
          return cnt
        res = 0
        if lead:
          res = __dfs(i + 1, cnt, False, True)

        up = num[i] if limit else 1
        low = 1 if lead else 0

        for j in range(low, up + 1):
          t = 0
          if j == 1 and (n - i) % x == 0:
            t = 1
          res += __dfs(i + 1, cnt + t, limit and j == up, False)

        return res

      return __dfs(0, 0, True, True)

    while l < r:
      mid = l + r + 1 >> 1
      res = dp(bin(mid)[2:])
      if res <= k:
        l = mid
      else:
        r = mid - 1
    return l
