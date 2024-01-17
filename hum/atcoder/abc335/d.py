n = int(input())
a = [[-1] * n for j in range(n)]

cur = 1

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = 0, 0
f = 0
while cur < n * n:
  a[x][y] = cur
  nx, ny = x + d[f][0], y + d[f][1]
  if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == -1:
    x, y = nx, ny
  else:
    f = (f + 1) % 4
    x, y = x + d[f][0], y + d[f][1]
  cur += 1

a[n // 2][n // 2] = 'T'

for i in a:
  print(*i)
