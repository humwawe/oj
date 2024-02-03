class FenwickTree:
  def __init__(self, n):
    self.N = n
    self.bit = [0] * n

  def get_sum(self, l, r):
    return self.__get_sum(r) - self.__get_sum(l - 1)

  def __get_sum(self, r):
    res = 0
    while r >= 0:
      res += self.bit[r]
      r = (r & (r + 1)) - 1
    return res

  def add(self, idx, v):
    while idx < self.N:
      self.bit[idx] += v
      idx = idx | (idx + 1)

  def get(self, idx):
    return self.get_sum(idx, idx)

  def set(self, idx, v):
    self.add(idx, v - self.get(idx))


n = int(input())
a = list(map(int, input().split()))

f = FenwickTree(n)
res = 0
for i in range(n):
  res += f.get_sum(a[i] - 1, n - 1)
  f.add(a[i] - 1, 1)

print(1 if res % 2 == 3 * n % 2 else 2)
