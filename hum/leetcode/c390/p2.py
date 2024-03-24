class Solution:
  def minOperations(self, k: int) -> int:
    res = k
    for i in range(1, k + 1):
      res = min(res, i - 1 + (k + i - 1) // i - 1)
    return res
