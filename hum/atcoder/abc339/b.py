h, w, n = map(int, input().split())
mat = [['.'] * w for _ in range(h)]

x, y = 0, 0
fs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
f = 0
for _ in range(n):
  if mat[x][y] == '.':
    mat[x][y] = '#'
    f = (f + 1) % 4
  elif mat[x][y] == '#':
    mat[x][y] = '.'
    f = (f - 1) % 4
  x += fs[f][0]
  y += fs[f][1]
  if x < 0:
    x = h - 1
  if x >= h:
    x = 0
  if y < 0:
    y = w - 1
  if y >= w:
    y = 0
for i in range(h):
  print(''.join(mat[i]))
