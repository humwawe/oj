from bisect import bisect_left
from typing import List


def z_function(s):
  n = len(s)
  z = [0] * n
  l, r = 0, 0
  for i in range(1, n):
    if i <= r and z[i - l] < r - i + 1:
      z[i] = z[i - l]
    else:
      z[i] = max(0, r - i + 1)
      while i + z[i] < n and s[z[i]] == s[i + z[i]]:
        z[i] += 1
    if i + z[i] - 1 > r:
      l = i
      r = i + z[i] - 1
  return z


class Solution:
  def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
    z1 = z_function(b + "#" + s)
    tmp = []
    for i in range(len(b) + 1, len(b + "#" + s)):
      if z1[i] >= len(b):
        tmp.append(i - (len(b) + 1))

    z2 = z_function(a + "#" + s)
    res = []
    for i in range(len(a) + 1, len(a + "#" + s)):
      if z2[i] >= len(a):
        j = i - (len(a) + 1)
        idx = bisect_left(tmp, j)
        if idx < len(tmp) and tmp[idx] - j <= k or idx - 1 >= 0 and j - tmp[idx - 1] <= k:
          res.append(j)
    return res
