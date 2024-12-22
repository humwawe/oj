class Solution:
  def minLength(self, s: str, numOps: int) -> int:
    n = len(s)
    cnt = 0
    for i in range(n):
      if int(s[i]) != i % 2:
        cnt += 1
    if min(cnt, n - cnt) <= numOps:
      return 1

    cnt = 1
    cur = []
    for i in range(1, n):
      if s[i] != s[i - 1]:
        cur.append(cnt)
        cnt = 1
      else:
        cnt += 1
    cur.append(cnt)
    l, r = 2, n
    while l < r:
      m = (l + r) // 2
      t = 0
      for x in cur:
        t += x // (m + 1)

      if t <= numOps:
        r = m
      else:
        l = m + 1
    return l
