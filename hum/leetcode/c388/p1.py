from typing import List


class Solution:
  def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
    m = sum(apple)
    capacity.sort(reverse=True)
    s = 0
    for i, v in enumerate(capacity):
      s += v
      if s >= m:
        return i + 1

    return -1
