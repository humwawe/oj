class Solution:
  def possibleStringCount(self, word: str) -> int:
    n = len(word)
    res = 1
    for i in range(1, n):
      if word[i] == word[i - 1]:
        res += 1
    return res
