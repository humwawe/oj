from bisect import bisect_right
from itertools import accumulate

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = list(accumulate(a))
for _ in range(q):
  x = int(input())
  idx = bisect_right(s, x)
  print(idx)
