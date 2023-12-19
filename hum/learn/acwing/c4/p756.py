n, m = map(int, input().split())
res = [[0 for j in range(m)] for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y, d = 0, 0, 1
for i in range(n * m):
  res[x][y] = i + 1
  a = x + dx[d]
  b = y + dy[d]
  if a < 0 or a >= n or b < 0 or b >= m or res[a][b] > 0:
    d = (d + 1) % 4
    a = x + dx[d]
    b = y + dy[d]
  x, y = a, b

for row in res:
  for x in row:
    print(x, end=' ')
  print()
