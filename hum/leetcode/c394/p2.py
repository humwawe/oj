from string import ascii_lowercase, ascii_uppercase


class Solution:
  def numberOfSpecialChars(self, word: str) -> int:
    res = 0
    s = set(word)
    for x, y in zip(ascii_lowercase, ascii_uppercase):
      if x in s and y in s:
        i = word.rfind(x)
        j = word.find(y)
        if i < j:
          res += 1
    return res
