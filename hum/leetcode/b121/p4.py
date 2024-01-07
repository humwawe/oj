from functools import cache


class Solution:
  def numberOfPowerfulInt(self, start: int, finish: int, lim: int, const_s: str) -> int:
    t1 = NumDp(finish, lim, const_s)
    t2 = NumDp(start - 1, lim, const_s)
    return t1.dp() - t2.dp()


class NumDp:
  def __init__(self, s_num, lim, const_s):
    self.s = s_num
    self.num = list(map(int, str(s_num)))
    self.n = len(self.num)
    self.lim = lim
    self.const_s = const_s
    self.diff = self.n - len(const_s)

  def dp(self):
    if int(self.s) < int(self.const_s):
      return 0
    return self.__dfs(0, True, True)

  @cache
  def __dfs(self, i, limit, lead):
    if i == self.n:
      return 0 if lead else 1

    res = 0
    # 可以跳过当前数位
    if lead:
      if i < self.diff:
        res = self.__dfs(i + 1, False, True)

    up = self.num[i] if limit else 9
    # 根据前导0判断是否能取到0
    low = 1 if lead else 0

    if i >= self.diff:
      j = int(self.const_s[i - self.diff])
      if low <= j <= min(self.lim, up):
        res = self.__dfs(i + 1, limit and j == up, False)
    else:
      for j in range(low, min(self.lim, up) + 1):
        res += self.__dfs(i + 1, limit and j == up, False)

    return res
