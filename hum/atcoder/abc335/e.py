from math import inf


class DJSet:

  def __init__(self, n):
    self.p = [-1] * n

  def find(self, x):
    if self.p[x] < 0:
      return x
    nx = x
    while self.p[x] >= 0:
      x = self.p[x]
    while nx != x:
      self.p[nx], nx = x, self.p[nx]
    return x

  def merge(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x != y:
      if self.p[y] < self.p[x]:
        x, y = y, x
      self.p[x] += self.p[y]
      self.p[y] = x
    return x == y

  def is_same(self, x, y):
    return self.find(x) == self.find(y)

  def is_root(self, x):
    return self.p[x] < 0

  def count(self):
    cnt = 0
    for i in self.p:
      if i < 0:
        cnt += 1
    return cnt

  def size(self, x):
    return -self.p[self.find(x)]

  def to_bucket(self):
    n = len(self.p)
    ret = [[] for _ in range(n)]
    for i in range(n):
      r = self.find(i)
      ret[r].append(i)
    return ret


n, m = map(int, input().split())
a = list(map(int, input().split()))
graph = [[] for _ in range(n)]
dj = DJSet(n)
tmp = []
for _ in range(m):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  tmp.append((u, v))
  if a[u] == a[v]:
    dj.merge(u, v)

for u, v in tmp:
  fu, fv = dj.find(u), dj.find(v)
  if fu != fv:
    if a[fu] < a[fv]:
      graph[fv].append(fu)
    else:
      graph[fu].append(fv)

dist = [-inf] * n
dist[dj.find(0)] = 1

for u in sorted(range(n), key=lambda x: a[x]):
  for v in graph[u]:
    dist[u] = max(dist[u], dist[v] + 1)

print(max(0, dist[dj.find(n - 1)]))
