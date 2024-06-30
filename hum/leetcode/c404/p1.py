class Solution:
  def maxHeightOfTriangle(self, red: int, blue: int) -> int:
    def f(a, b):
      cur = 0
      flag = 0
      while True:
        if flag == 0:
          if a > cur:
            cur += 1
            a -= cur
          else:
            break
          flag = 1
        else:
          if b > cur:
            cur += 1
            b -= cur
          else:
            break
          flag = 0
      return cur

    return max(f(red, blue), f(blue, red))
