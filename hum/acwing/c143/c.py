grid = [input() for _ in range(2)]
n = len(grid[0])
inf = float('inf')
dp0, dp1, dp2, dp3 = -inf, -inf, -inf, 0
for i in range(n):
  t = grid[0][i] + grid[1][i]
  if t == '00':
    dp0, dp1, dp2, dp3 = max(dp0, dp1, dp2, dp3), dp0 + 1, dp0 + 1, max(dp0, dp1, dp2) + 1
  elif t == '01':
    dp0, dp1, dp2, dp3 = -inf, -inf, max(dp0, dp1, dp2, dp3), dp0 + 1
  elif t == '10':
    dp0, dp1, dp2, dp3 = -inf, max(dp0, dp1, dp2, dp3), -inf, dp0 + 1
  else:
    dp0, dp1, dp2, dp3 = -inf, -inf, -inf, max(dp0, dp1, dp2, dp3)

print(max(dp0, dp1, dp2, dp3))
