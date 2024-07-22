class Solution:
  def maxOperations(self, s: str) -> int:
    n = len(s)
    s += '1'
    cnt = 0
    res = 0
    for i in range(n - 1, -1, -1):
      if s[i] == '0':
        if s[i + 1] == '1':
          cnt += 1
      else:
        res += cnt
    return res
