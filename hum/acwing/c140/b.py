n = int(input())
a = list(map(int, input().split()))
if n == 1:
  print(0)
else:
  res = float('inf')
  for i in range(-1, 2):
    for j in range(-1, 2):
      x, y = a[0] + i, a[1] + j
      d = y - x
      tmp = abs(i) + abs(j)
      for k in range(2, n):
        z = a[k]
        diff = 2 * y - x - z
        if -1 <= diff <= 1:
          z += diff
          tmp += abs(diff)
        else:
          break
        x, y = y, z
      else:
        res = min(res, tmp)

  print(-1 if res == float('inf') else res)
