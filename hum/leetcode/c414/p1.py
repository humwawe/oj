class Solution:
  def convertDateToBinary(self, date: str) -> str:
    ss = date.split('-')
    res = []
    for i in ss:
      res.append(bin(int(i))[2:])
    return '-'.join(res)
