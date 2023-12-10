from typing import List


class Solution:
  def countTestedDevices(self, batteryPercentages: List[int]) -> int:
    cnt = 0
    res = 0
    for i in batteryPercentages:
      if i - cnt > 0:
        res += 1
        cnt += 1
    return res
