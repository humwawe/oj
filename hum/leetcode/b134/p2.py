from typing import List


class Solution:
  def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
    n = len(enemyEnergies)
    enemyEnergies.sort()
    if currentEnergy < enemyEnergies[0]:
      return 0
    currentEnergy += sum(enemyEnergies[1:])

    return currentEnergy // enemyEnergies[0]
