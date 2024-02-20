from typing import List


class Solution:
  def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
    n, m = len(nums), len(pattern)
    tmp = []
    for i in range(n - 1):
      if nums[i] == nums[i + 1]:
        tmp.append(0)
      elif nums[i] > nums[i + 1]:
        tmp.append(-1)
      else:
        tmp.append(1)

    pattern.append(2)
    pattern.extend(tmp)

    def z_function(s):
      n = len(s)
      z = [0] * n
      l, r = 0, 0
      for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
          z[i] = z[i - l]
        else:
          z[i] = max(0, r - i + 1)
          while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
          l = i
          r = i + z[i] - 1
      return z

    z_res = z_function(pattern)
    return sum(z_res[i] == m for i in range(m, len(pattern)))
