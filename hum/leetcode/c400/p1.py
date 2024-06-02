class Solution:
  def minimumChairs(self, s: str) -> int:
    res = 0
    cur = 0
    for x in s:
      if x == 'E':
        cur += 1
      else:
        cur -= 1
      res = max(res, cur)

    return res
