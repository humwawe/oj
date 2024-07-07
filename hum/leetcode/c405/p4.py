from math import inf
from typing import List


class Solution:
  def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
    n = len(target)
    m = len(words)
    dp = [inf] * (n + 1)

    d = dict()
    l = set()
    for i in range(m):
      word = words[i]
      l.add(len(word))
      d[word] = min(costs[i], d.get(word, inf))

    dp[0] = 0
    for i in range(1, n + 1):
      for length in l:
        if i - length >= 0 and dp[i - length] + d.get(target[i - length:i], inf) < dp[i]:
          dp[i] = dp[i - length] + d.get(target[i - length:i], inf)

    return -1 if dp[n] == inf else dp[n]
