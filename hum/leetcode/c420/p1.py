from typing import List


class Solution:
  def stringSequence(self, target: str) -> List[str]:
    res = []
    for i in range(len(target)):
      cur = target[i]
      if len(res) == 0:
        for j in range(ord(cur) - ord('a') + 1):
          res.append(chr(ord('a') + j))
      else:
        t = res[-1]
        for j in range(ord(cur) - ord('a') + 1):
          res.append(t + chr(ord('a') + j))
    return res
