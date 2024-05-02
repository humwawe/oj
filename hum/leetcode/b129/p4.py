class Solution:
  def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    mod = 10 ** 9 + 7
    dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

    for i in range(min(zero, limit) + 1):
      dp[i][0][0] = 1
    for i in range(min(one, limit) + 1):
      dp[0][i][1] = 1

    sum1 = [0] * (one + 1)
    for i in range(one + 1):
      sum1[i] = dp[0][i][1]

    for i in range(1, zero + 1):
      sum0 = dp[i][0][0]
      for j in range(1, one + 1):
        dp[i][j][0] = sum1[j]
        dp[i][j][1] = sum0

        sum0 = (sum0 + dp[i][j][0]) % mod
        if j - limit >= 0:
          sum0 = (sum0 - dp[i][j - limit][0]) % mod

        sum1[j] = (sum1[j] + dp[i][j][1]) % mod
        if i - limit >= 0:
          sum1[j] = (sum1[j] - dp[i - limit][j][1]) % mod

    return (dp[zero][one][0] + dp[zero][one][1]) % mod


solu = Solution()
print(solu.numberOfStableArrays(zero=1, one=1, limit=2))
