class Solution:
  def countWinningSequences(self, s: str) -> int:
    n = len(s)
    base = n
    dp = [[[0] * 3 for _ in range(2 * n + 1)] for _ in range(n)]
    tmp1 = {'F': 0, 'E': 1, 'W': 2}
    s = [tmp1[x] for x in s]

    dp[0][0 + base][s[0]] = 1
    dp[0][1 + base][(s[0] - 1) % 3] = 1
    dp[0][-1 + base][(s[0] + 1) % 3] = 1

    def f(x, y):
      if x == y:
        return 0
      if (x + 1) % 3 == y:
        return -1
      if (x - 1) % 3 == y:
        return 1

    mod = 10 ** 9 + 7
    for i in range(1, n):
      for j in range(-n, n + 1, 1):
        for k in range(3):
          if dp[i - 1][j + base][k] != 0:
            for l in range(3):
              if k == l:
                continue
              if -n <= j + f(s[i], l) <= n:
                dp[i][j + f(s[i], l) + base][l] += dp[i - 1][j + base][k]
                dp[i][j + f(s[i], l) + base][l] %= mod

    res = 0
    for i in range(1, n + 1):
      for j in range(3):
        res = (res + dp[-1][i + base][j]) % mod
    return res


s = Solution()
print(s.countWinningSequences("FFF"))
