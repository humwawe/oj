from itertools import pairwise, accumulate

n, m = map(int, input().split())
a = list(map(int, input().split()))

diff = [0] * (n + 1)
for x, y in pairwise(a):
  if x > y:
    x, y = y, x
  diff[0] += y - x
  diff[x] -= y - x
  diff[x] += n - (y - x)
  diff[y] -= n - (y - x)
  diff[y] += y - x
  diff[n] -= y - x

cum = list(accumulate(diff))
print(min(cum[:n]))
