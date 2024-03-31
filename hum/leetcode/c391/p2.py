class Solution:
  def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
    cur = [numBottles, 0, numExchange, 0]
    while True:
      while cur[1] >= cur[2]:
        cur[0] += 1
        cur[1] -= cur[2]
        cur[2] += 1

      if cur[0] == 0:
        break

      if cur[0] > 0:
        cur[1] += cur[0]
        cur[3] += cur[0]
        cur[0] = 0

    return cur[3]
