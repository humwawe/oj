class Solution:
  def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
    n = len(s)
    length = n // k
    t1 = []
    t2 = []
    for i in range(0, n, length):
      t1.append(s[i:i + length])
      t2.append(t[i:i + length])

    t1.sort()
    t2.sort()
    return t1 == t2
