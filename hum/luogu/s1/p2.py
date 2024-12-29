t = int(input())


def dfs(p, q, k):
  if k == 1:
    return p + q, p
  x, y = dfs(p, q, k - 1)
  return x + y, x


for _ in range(t):
  n = int(input())
  res = dfs(1, 1, n)
  if max(res) > 10 ** 18:
    print(-1)
    continue
  print(*res)
