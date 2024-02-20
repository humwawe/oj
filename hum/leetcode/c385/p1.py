from typing import List


class Solution:
  def countPrefixSuffixPairs(self, words: List[str]) -> int:
    n = len(words)

    def f(s, t):
      return t.startswith(s) and t.endswith(s)

    res = 0
    for i in range(n):
      for j in range(i + 1, n):
        if f(words[i], words[j]):
          res += 1
    return res
