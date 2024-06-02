from typing import List


class Solution:
  def countDays(self, days: int, meetings: List[List[int]]) -> int:
    meetings.sort()
    last = 0
    res = 0
    for s, t in meetings:
      if s <= last + 1:
        last = max(last, t)
      else:
        res += s - (last + 1)
        last = t

    if last < days:
      res += days - last
    return res
