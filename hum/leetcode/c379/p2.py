class Solution:
  def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    if a == e:
      if a != c or d < min(b, f) or d > max(b, f):
        return 1

    if b == f:
      if b != d or c < min(a, e) or c > max(a, e):
        return 1

    if c + d == e + f:
      if c + d != a + b or a < min(c, e) or a > max(c, e):
        return 1
    if c - d == e - f:
      if c - d != a - b or a < min(c, e) or a > max(c, e):
        return 1
    return 2
