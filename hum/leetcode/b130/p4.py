from typing import List


class Solution:
  def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:

    def f(x):
      l, r = 0, x
      while l < r:
        m = (l + r) // 2
        cnt = 0
        val = 1
        while val <= m:
          a, b = divmod(m, val * 2)
          cnt += a * val + max(b - val + 1, 0)
          val *= 2
        if cnt >= x:
          r = m
        else:
          l = m + 1

      l -= 1
      res = 0
      val = 1
      tmp = 0
      resid = x
      while val <= l:
        a, b = divmod(l, val * 2)
        cnt = a * val + max(b - val + 1, 0)
        resid -= cnt
        res += cnt * tmp
        val *= 2
        tmp += 1

      v = l + 1
      for _ in range(resid):
        x = v & -v
        res += x.bit_length() - 1
        v -= x
      return res

    res = []
    for l, r, mod in queries:
      res.append(pow(2, f(r + 1) - f(l), mod))
    return res
