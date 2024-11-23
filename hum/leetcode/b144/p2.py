from typing import List


class Solution:
  def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
    tmp = [[0] * 26 for _ in range(26)]
    for i in range(26):
      for j in range(26):
        k = i
        s1 = 0
        while k != j:
          s1 += nextCost[k]
          k = (k + 1) % 26

        k = i
        s2 = 0
        while k != j:
          s2 += previousCost[k]
          k -= 1
          k %= 26

        tmp[i][j] = min(s1, s2)

    res = 0
    for a, b in zip(s, t):
      res += tmp[ord(a) - ord('a')][ord(b) - ord('a')]
    return res
