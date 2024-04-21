from string import ascii_lowercase, ascii_uppercase


class Solution:
  def numberOfSpecialChars(self, word: str) -> int:
    res = 0
    for x, y in zip(ascii_lowercase, ascii_uppercase):
      if x in word and y in word:
        res += 1
    return res
