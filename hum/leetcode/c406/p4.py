class Solution:
  def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
    tmp = []
    for h in horizontalCut:
      tmp.append((h, 0))
    for v in verticalCut:
      tmp.append((v, 1))
    tmp.sort(key=lambda x: x[0], reverse=True)

    res = 0
    c1, c2 = 1, 1
    for v, t in tmp:
      if t == 0:
        c1 += 1
        res += c2 * v
      else:
        c2 += 1
        res += c1 * v
    return res
