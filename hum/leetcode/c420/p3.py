from typing import List

N = 10 ** 6
max_pr = list(range(N + 1))

for i in range(2, N + 1):
  if max_pr[i] == i:
    for j in range(i, N + 1, i):
      max_pr[j] = i

max_div = [1] * (N + 1)
for i in range(2, N + 1):
  if i == max_pr[i]:
    max_div[i] = -1
  else:
    t = i
    while t != max_pr[t]:
      max_div[i] *= max_pr[t]
      t //= max_pr[t]


class Solution:
  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    last = 10 ** 8
    res = 0
    for i in range(n - 1, -1, -1):

      while nums[i] > last:
        if max_div[nums[i]] == -1:
          return -1
        nums[i] = nums[i] // max_div[nums[i]]
        res += 1
      last = nums[i]

    return res


s = Solution()
print(s.minOperations([25, 7]))
