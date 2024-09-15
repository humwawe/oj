from typing import List


class Solution:
  def maxValue(self, nums: List[int], k: int) -> int:
    n = len(nums)
    m = 2 ** 7
    pre = [[0] * (k + 1) for _ in range(n)]
    pre[0][0] = 1
    pre[0][1] = 1 << nums[0]
    for i in range(1, n):
      for j in range(k + 1):
        pre[i][j] = pre[i - 1][j]
        if j:
          for l in range(m):
            if pre[i - 1][j - 1] >> l & 1 == 1:
              pre[i][j] |= 1 << (l | nums[i])

    b = nums[::-1]

    suf = [[0] * (k + 1) for _ in range(n)]
    suf[0][0] = 1
    suf[0][1] = 1 << b[0]
    for i in range(1, n):
      for j in range(k + 1):
        suf[i][j] = suf[i - 1][j]
        if j:
          for l in range(m):
            if suf[i - 1][j - 1] >> l & 1 == 1:
              suf[i][j] |= 1 << (l | b[i])

    res = 0
    for i in range(k - 1, n - k):
      x = pre[i][k]
      y = suf[n - i - 2][k]
      for j in range(1, m):
        if x >> j & 1 == 1:
          for l in range(1, m):
            if y >> l & 1 == 1:
              res = max(res, j ^ l)
    return res


s = Solution()
print(s.maxValue([8, 114], 1))
