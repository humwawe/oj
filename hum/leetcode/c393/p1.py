class Solution:
  def findLatestTime(self, s: str) -> str:
    res = []
    for i in range(11, -1, -1):
      tmp = str(i).zfill(2)
      if (s[0] == '?' or s[0] == tmp[0]) and (s[1] == '?' or s[1] == tmp[1]):
        res.append(tmp)
        break
    res.append(":")
    for i in range(59, -1, -1):
      tmp = str(i).zfill(2)
      if (s[3] == '?' or s[3] == tmp[0]) and (s[4] == '?' or s[4] == tmp[1]):
        res.append(tmp)
        break
    return ''.join(res)
