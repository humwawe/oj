class Solution:
  def compressedString(self, word: str) -> str:
    i = 0
    n = len(word)
    res = []
    while i < n:
      j = i
      while j + 1 < n and word[j + 1] == word[i]:
        j += 1
      l = j - i + 1

      while l >= 9:
        res.append('9')
        res.append(word[i])
        l -= 9
      if l > 0:
        res.append(str(l))
        res.append(word[i])
      i = j + 1

    return "".join(res)
