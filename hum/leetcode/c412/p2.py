from typing import List


class Solution:
  def countPairs(self, nums: List[int]) -> int:

    n = len(nums)
    res = 0
    nums.sort(reverse=True)

    def check(a, b):
      if a == b:
        return True
      a = list(str(a))

      n = len(a)
      for i in range(n):
        for j in range(i):
          a[i], a[j] = a[j], a[i]
          if int(''.join(a)) == b:
            return True
          a[j], a[i] = a[i], a[j]
      return False

    for i in range(n):
      for j in range(i):
        if check(nums[i], nums[j]):
          res += 1

    return res
