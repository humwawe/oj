from typing import List


class Solution:
  def sumOfEncryptedInt(self, nums: List[int]) -> int:
    res = 0
    for num in nums:
      s = str(num)
      s = max(s) * len(s)
      
      res += int(s)
    return res
