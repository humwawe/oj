from heapq import heappush, heappop

n, m = map(int, input().split())

orders = [[] for _ in range(n)]

res = [-1] * n
f = 1
for i in range(m):
  s, d, c = map(int, input().split())
  s -= 1
  d -= 1

  if res[d] == -1:
    f = 0
  res[d] = m
  orders[s].append((d, c, i))

if f:
  print(-1)


def work():
  hpq = []
  for i in range(n):
    for v in orders[i]:
      heappush(hpq, v)

    if hpq and hpq[0][0] == i:
      print(-1)
      return

    if res[i] == -1 and hpq:
      d, c, idx = heappop(hpq)
      res[i] = idx
      c -= 1
      if c:
        heappush(hpq, (d, c, idx))

  print(*(x + 1 for x in res))
  return


work()
