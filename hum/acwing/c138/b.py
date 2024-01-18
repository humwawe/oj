from bisect import bisect_left, bisect_right
from itertools import accumulate

n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s_a = list(accumulate(a))
cur = 0
for num in b:
  cur += num
  idx = bisect_right(s_a, cur)
  if cur >= s_a[-1]:
    cur = 0
    print(n)
  else:
    print(n - idx)
