import sys

input = lambda: sys.stdin.readline().rstrip()
t = int(input())


def s():
  r1, r2 = n, -1
  c1, c2 = m, -1
  cnt = 0
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1:
        cnt += 1
        r1 = min(r1, i)
        r2 = max(r2, i)
        c1 = min(c1, j)
        c2 = max(c2, j)

  if r1 != 0 or c1 != 0 or r2 != n - 1 or c2 != m - 1:
    print(-1)
    return
  if cnt == n * m:
    print(0)
    return
  if (grid[0][0] == 1 and grid[-1][-1] == 1) or (grid[-1][0] == 1 and grid[0][-1]) == 1:
    print(1)
    return
  if grid[0][0] == 1 or grid[-1][-1] == 1 or grid[-1][0] == 1 or grid[0][-1] == 1:
    print(2)
    return

  print(3)


for _ in range(t):
  n, m = map(int, input().split())
  grid = [[int(x) for x in (input())] for _ in range(n)]
  # grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  # for i in range(16):
  #   for j in range(16):
  #     for k in range(16):
  #       for l in range(16):
  #         for z in range(4):
  #           grid[0][z] = (i >> z) & 1
  #           grid[1][z] = (j >> z) & 1
  #
  #           grid[2][z] = (k >> z) & 1
  #           grid[3][z] = (l >> z) & 1

  s()
