from collections import Counter
from sys import stdin

for s in stdin.readlines():
  res = Counter()
  for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
      t = s[i:j]
      res[t] += 1

  for x, y in sorted(res.items()):
    if y != 1:
      print(x, y)
