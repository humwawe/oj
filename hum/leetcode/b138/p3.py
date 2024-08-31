import math


class Solution:
  def countGoodIntegers(self, n: int, k: int) -> int:
    if n == 1:
      res = 0
      for i in range(1, 10):
        if i % k == 0:
          res += 1
      return res

    pow = [1] * n
    for i in range(1, n):
      pow[i] = pow[i - 1] * 10 % k

    def f(s):
      cnt = [0] * 10
      for i in range(n):
        cnt[int(s[i])] += 1
      return '#'.join(map(str, cnt))

    st = set()
    low = 10 ** (n // 2 - 1)
    high = 10 ** (n // 2)
    mid = True if n % 2 else False
    if mid:
      for i in range(low, high):
        for j in range(10):
          cur = str(i) + str(j) + str(i)[::-1]
          m = 0
          for idx in range(n):
            m = (m + pow[-1 - idx] * int(cur[idx])) % k
          if m == 0:
            st.add(f(cur))
    else:
      for i in range(low, high):
        cur = str(i) + str(i)[::-1]

        m = 0
        for idx in range(n):
          m = (m + pow[-1 - idx] * int(cur[idx])) % k
        if m == 0:
          st.add(f(cur))
    res = 0
    for c in st:
      cnt = c.split('#')
      cnt = [int(i) for i in cnt]
      t = math.comb(n - 1, cnt[0])
      ln = n - cnt[0]
      x = math.perm(ln, ln)
      for i in range(1, 10):
        x //= math.perm(cnt[i], cnt[i])
      res += t * x

    return res


s = Solution()
print(s.countGoodIntegers(n=10, k=4))
