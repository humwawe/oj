class Solution:
  def clearDigits(self, s: str) -> str:
    res = []
    for x in s:
      if "0" <= x <= "9":
        res.pop()
      else:
        res.append(x)

    return ''.join(res)
