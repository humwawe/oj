from typing import List


class Solution:
  def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    tmp, res = 0, 0
    for dim in dimensions:
      if dim[0] * dim[0] + dim[1] * dim[1] > tmp:
        tmp = dim[0] * dim[0] + dim[1] * dim[1]
        res = dim[0] * dim[1]
      elif dim[0] * dim[0] + dim[1] * dim[1] == tmp:
        res = max(res, dim[0] * dim[1])

    return res
