class Solution:
  def numberOfChild(self, n: int, k: int) -> int:
    cur = 0
    f = 1
    for i in range(k):
      cur = cur + f
      if cur == n:
        f = -1
        cur = n - 2
      if cur == -1:
        f = 1
        cur = 1
    return cur
