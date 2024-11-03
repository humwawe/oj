from collections import Counter
from math import comb


class Solution:
  def countBalancedPermutations(self, num: str) -> int:
    num = [int(i) for i in num]

    s = sum(num)
    if s % 2 != 0:
      return 0
    m = s // 2
    c = len(num) // 2
    o_c = len(num) - c
    cnt = Counter(num)
    dp = [[0] * (m + 1) for _ in range(c + 1)]
    vis = [[0] * (m + 1) for _ in range(c + 1)]
    dp[0][0] = 1
    vis[0][0] = 1
    acc = [0]
    for x in range(10):
      acc.append(acc[-1] + cnt[x])
    mod = 10 ** 9 + 7
    for x in range(10):
      if cnt[x]:
        for cur_c in range(cnt[x] + 1):
          for pre_c in range(c + 1):
            for pre_v in range(m + 1):
              if vis[pre_c][pre_v]:
                nc = cur_c + pre_c
                if nc > c:
                  continue
                nv = pre_v + x * cur_c
                if nv > m:
                  continue
                if o_c - (acc[x] - pre_c) < 0:
                  continue
                vis[nc][nv] = 1
                dp[nc][nv] = (dp[nc][nv] + dp[pre_c][pre_v] * comb(cur_c, c - pre_c)
                              * comb(cnt[x] - cur_c, o_c - (acc[x] - pre_c))) % mod

    return dp[c][m]


s = Solution()
print(s.countBalancedPermutations("123"))
