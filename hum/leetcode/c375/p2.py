from typing import List


class Solution:
  def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
    res = []
    for i, v in enumerate(variables):
      if pow(pow(v[0], v[1], 10), v[2], v[3]) == target:
        res.append(i)
    return res
