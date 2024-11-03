class Solution:
  def isBalanced(self, num: str) -> bool:
    n = len(num)
    res = 0
    for i in range(n):
      if i % 2:
        res += int(num[i])
      else:
        res -= int(num[i])
    return res == 0
