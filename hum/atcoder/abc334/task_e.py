from collections import deque

n, m = map(int, input().split())
a = ["" for _ in range(n)]
for i in range(n):
  a[i] = input()

color = [[-1] * m for _ in range(n)]
cur = 0
c_red = 0
for i in range(n):
  for j in range(m):
    if a[i][j] == '#' and color[i][j] == -1:
      color[i][j] = cur
      que = deque()
      que.append((i, j))
      while que:
        x, y = que.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
          nx = x + dx
          ny = y + dy
          if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == '#' and color[nx][ny] == -1:
            que.append((nx, ny))
            color[nx][ny] = cur
      cur += 1
    elif a[i][j] == '.':
      c_red += 1

cnt = cur
res = 0
for i in range(n):
  for j in range(m):
    if a[i][j] == '.':
      s = set()
      for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        x = i + dx
        y = j + dy
        if 0 <= x < n and 0 <= y < m:
          s.add(color[x][y])
      s.discard(-1)
      if len(s) >= 1:
        res += cnt - (len(s) - 1)
      else:
        res += cnt + 1

mod = 998244353
c_red = pow(c_red, mod - 2, mod)

print(res * c_red % mod)
