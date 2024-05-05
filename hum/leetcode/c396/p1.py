from string import ascii_lowercase


class Solution:
  def isValid(self, word: str) -> bool:
    if '@' in word or '#' in word or '$' in word:
      return False
    if len(word) < 3:
      return False
    word = word.lower()
    res = 0
    for c in word:
      if c in 'aeiou':
        res |= 1
      elif c in ascii_lowercase:
        res |= 2
    return res == 3
