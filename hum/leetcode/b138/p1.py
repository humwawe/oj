class Solution:
  def generateKey(self, num1: int, num2: int, num3: int) -> int:
    a, b, c = str(num1).zfill(4), str(num2).zfill(4), str(num3).zfill(4)
    res = ""
    for i in range(4):
      res += min(a[i], b[i], c[i])
    return int(res)
