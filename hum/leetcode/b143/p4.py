from functools import cache
from math import gcd


class Solution:
  def smallestNumber(self, s: str, t: int) -> str:
    tmp = t
    cnt = 0
    for p in 2, 3, 5, 7:
      while tmp % p == 0:
        tmp //= p
        cnt += 1
    if tmp > 1:  # t 包含其他质因子
      return "-1"

    # 补前导零（至少一个）
    cnt = max(cnt - len(s) + 1, 1)
    s = '0' * cnt + s

    n = len(s)
    ans = ['0'] * n

    @cache  # 仅仅作为 vis 标记使用
    def dfs(i: int, t: int, is_limit: bool) -> bool:
      if i == n:
        return t == 1

      if is_limit and i < cnt and dfs(i + 1, t, True):  # 填 0（跳过）
        return True

      low = int(s[i]) if is_limit else 0
      for d in range(max(low, 1), 10):
        if dfs(i + 1, t // gcd(t, d), is_limit and d == low):
          ans[i] = str(d)
          return True
      return False

    dfs(0, t, True)
    dfs.cache_clear()  # 防止爆内存
    return ''.join(ans).lstrip('0')  # 去掉前导零
