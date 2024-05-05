from collections import Counter


class Solution:
  def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
    n = len(word)
    cnt = Counter()
    for i in range(0, n, k):
      cnt[word[i:i + k]] += 1

    return n // k - max(cnt.values())
