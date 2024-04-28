class Solution:
  def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    n = zero + one
    dp = [[[0] * (zero + 1) for _ in range(limit + 1)] for _ in range(2)]
    dp[0][0][0] = 1

    mod = 10 ** 9 + 7
    for i in range(1, n + 1):
      ndp = [[[0] * (zero + 1) for _ in range(limit + 1)] for _ in range(2)]
      for v in range(2):
        for l in range(limit + 1):
          for c in range(zero + 1):
            if dp[v][l][c] == 0: continue
            if v == 0:
              if c < zero and l < limit:
                ndp[0][l + 1][c + 1] += dp[v][l][c]
                if ndp[0][l + 1][c + 1] >= mod:
                  ndp[0][l + 1][c + 1] -= mod
              if i - c - 1 < one:
                ndp[1][1][c] += dp[v][l][c]
                if ndp[1][1][c] >= mod:
                  ndp[1][1][c] -= mod
            else:
              if c < zero:
                ndp[0][1][c + 1] += dp[v][l][c]
                if ndp[0][1][c + 1] >= mod:
                  ndp[0][1][c + 1] -= mod
              if i - c - 1 < one and l < limit:
                ndp[1][l + 1][c] += dp[v][l][c]
                if ndp[1][l + 1][c] >= mod:
                  ndp[1][l + 1][c] %= mod
      dp = ndp

    res = 0
    for v in range(2):
      for l in range(limit + 1):
        for c in range(zero + 1):
          res += dp[v][l][c]
          if res >= mod:
            res -= mod
    return res
