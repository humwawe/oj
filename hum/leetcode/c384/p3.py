from collections import Counter
from typing import List


class Solution:
  def maxPalindromesAfterOperations(self, words: List[str]) -> int:
    n = len(words)
    cnt = Counter()
    for i in range(n):
      cnt += Counter(words[i])

    v = sum(v // 2 for v in cnt.values())
    words.sort(key=len)
    res = 0
    for w in words:
      tmp_l = len(w) // 2
      if tmp_l > v:
        break
      v -= tmp_l
      res += 1
    return res
