class Solution:
  def stringHash(self, s: str, k: int) -> str:
    n = len(s)
    m = n // k
    tmp = [0] * (m)

    for i in range(n):
      tmp[i // k] += ord(s[i]) - ord('a')

    res = []
    for i in range(m):
      res.append(chr(ord('a') + tmp[i] % 26))
    return ''.join(res)
