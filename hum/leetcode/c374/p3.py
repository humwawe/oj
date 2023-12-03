from collections import Counter


class Solution:
  def countCompleteSubstrings(self, word: str, k: int) -> int:
    def helper(w):
      n = len(w)
      res = 0
      for j in range(1, 27):
        size = j * k
        if size > n:
          break
        c = Counter(w[:size])
        if all(j == k for j in c.values()):
          res += 1
        for x, y in zip(w, w[size:]):
          c[x] -= 1
          c[y] += 1
          if all(j == 0 or j == k for j in c.values()):
            res += 1
      return res

    n = len(word)
    w = [ord(c) - ord('a') for c in word]
    i = 0
    res = 0
    while i < n:
      j = i
      while j + 1 < n and abs(w[j + 1] - w[j]) <= 2:
        j += 1
      res += helper(w[i:j + 1])
      i = j + 1
    return res
