from functools import cache


def dp(s_num, ds):
  num = list(map(int, str(s_num)))
  n = len(num)

  @cache
  def __dfs(i, cur, dig_sum, limit, lead):
    if dig_sum > ds:
      return 0

    if i == n:
      if dig_sum == ds and cur == 0:
        return 0 if lead else 1
      return 0

    res = 0
    if lead:
      res = __dfs(i + 1, cur, dig_sum, False, True)

    up = num[i] if limit else 9
    low = 1 if lead else 0

    for j in range(low, up + 1):
      res += __dfs(i + 1, (cur * 10 + j) % ds, dig_sum + j, limit and j == up, False)
    return res

  return __dfs(0, 0, 0, True, True)


n = int(input())
max_sum = 9 * 14

res = 0
for ds in range(1, max_sum + 1):
  res += dp(str(n), ds)

print(res)
