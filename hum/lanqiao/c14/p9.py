n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

x, y = 1, 1
if n % 3 != 0:
  x = 0
if m % 3 != 0:
  y = 0

res = 0
for i in range(n):
  for j in range(m):
    if (i - x) % 3 == 0 and (j - y) % 3 == 0:
      res += grid[i][j]

print(res)
