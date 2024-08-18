class Solution:
  def largestPalindrome(self, n: int, k: int) -> str:
    s = list("9" * n)
    if k == 2:
      s[0] = s[-1] = "8"
    if k == 4:
      if n == 1:
        return "8"
      else:
        s[0] = s[-1] = s[1] = s[-2] = "8"
    if k == 5:
      s[0] = s[-1] = "5"
    if k == 6:
      s[0] = s[-1] = "8"
      if n == 1:
        s[0] = "6"
      elif n == 2:
        s[0] = s[-1] = "6"
      else:
        if n % 2 == 1:
          s[n // 2] = "8"
        else:
          s[n // 2] = s[n // 2 - 1] = "7"
    if k == 7:
      if n == 1:
        s[0] = "7"
      elif n == 2:
        s[0] = s[-1] = "7"
      elif n == 3:
        s[1] = "5"
      elif n == 4:
        s[1] = s[2] = "7"
      elif n == 5:
        s[2] = "7"
      elif n == 6:
        pass
      elif n == 7:
        s[3] = "4"
      elif n == 8:
        s[3] = s[4] = "4"
      else:
        for i in range(9, -1, -1):
          if n % 2 == 1:
            s[n // 2] = str(i)
          else:
            s[n // 2] = s[n // 2 - 1] = str(i)
          cur = 0
          for i in range(n):
            cur = (cur * 10 + int(s[i])) % 7
          if cur == 0:
            break
    if k == 8:
      if n == 1:
        s[0] = "8"
      elif n == 2:
        s[0] = s[-1] = "8"
      elif n == 3:
        s[0] = s[-1] = s[1] = "8"
      else:
        for i in range(3):
          s[i] = s[-1 - i] = "8"
    return "".join(s)
