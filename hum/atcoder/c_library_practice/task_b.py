class FenwickTree:
  def __init__(self, n):
    self.n = n
    self.bit = [0] * n

  def get_sum(self, r):
    res = 0
    while r >= 0:
      res += self.bit[r]
      r = (r & (r + 1)) - 1
    return res

  def add(self, idx, v):
    while idx < self.n:
      self.bit[idx] += v
      idx = idx | (idx + 1)

  def get_range_sum(self, l, r):
    return self.get_sum(r) - self.get_sum(l - 1)

  def get(self, idx):
    return self.get_range_sum(idx, idx)

  def set(self, idx, v):
    self.add(idx, v - self.get(idx))


n, q = map(int, input().split())
a = list(map(int, input().split()))
f = FenwickTree(n)
for i, v in enumerate(a):
  f.add(i, v)
for _ in range(q):
  t, x, y = map(int, input().split())
  if t == 0:
    f.add(x, y)
  else:
    print(f.get_range_sum(x, y - 1))
