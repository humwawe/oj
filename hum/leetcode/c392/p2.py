from string import ascii_lowercase


class Solution:
  def getSmallestString(self, s: str, k: int) -> str:
    t = [c for c in s]

    def dif(a, b):
      if a > b:
        a, b = b, a
      return min(ord(b) - ord(a), 26 + ord(a) - ord(b))

    diff = 0
    for i, v in enumerate(s):
      for a in ascii_lowercase:
        if diff + dif(a, v) <= k:
          t[i] = a
          diff += dif(a, v)
          break

    return "".join(t)
