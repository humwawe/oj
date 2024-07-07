from typing import List


class Solution:
  def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
    n = len(colors)
    colors.extend(colors[:k])
    s = [0]
    for i in range(1, len(colors)):
      if colors[i] != colors[i - 1]:
        s.append(s[-1] + 1)
      else:
        s.append(s[-1])

    res = 0
    for i in range(n):
      if s[i + k - 1] - s[i] == k - 1:
        res += 1
    return res
