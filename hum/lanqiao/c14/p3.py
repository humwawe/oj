import sys
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s = input()
a = []
for i in range(n):
  if s[i] == '1' and (i + 1 < n and s[i + 1] == '0'):
    a.append(1)
  else:
    a.append(0)

acc = list(accumulate(a, initial=0))

q = int(input())
for _ in range(q):
  l, r = map(lambda x: int(x) - 1, input().split())
  print(acc[r] - acc[l])
