class Solution:
  def minDifference(self, nums: List[int]) -> int:
    n = len(nums)
    # 和空位相邻的最小数字 min_l 和最大数字 max_r
    min_l, max_r = inf, 0
    for i, v in enumerate(nums):
      if v != -1 and (i > 0 and nums[i - 1] == -1 or i < n - 1 and nums[i + 1] == -1):
        min_l = min(min_l, v)
        max_r = max(max_r, v)

    def calc_diff(l: int, r: int, big: bool) -> int:
      d = (min(r - min_l, max_r - l) + 1) // 2
      if big:
        d = min(d, (max_r - min_l + 2) // 3)  # d 不能超过上界
      return d

    ans = 0
    pre_i = -1
    for i, v in enumerate(nums):
      if v == -1:
        continue
      if pre_i >= 0:
        if i - pre_i == 1:
          ans = max(ans, abs(v - nums[pre_i]))
        else:
          ans = max(ans, calc_diff(min(nums[pre_i], v), max(nums[pre_i], v), i - pre_i > 2))
      elif i > 0:
        ans = max(ans, calc_diff(v, v, False))
      pre_i = i
    if 0 <= pre_i < n - 1:
      ans = max(ans, calc_diff(nums[pre_i], nums[pre_i], False))
    return ans
