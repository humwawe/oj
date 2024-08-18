from typing import List


class Solution:
  def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
    n = len(energyDrinkA)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = energyDrinkA[0]
    dp[0][1] = energyDrinkB[0]
    for i in range(1, n):
      dp[i][0] = max(dp[i - 1][0] + energyDrinkA[i], dp[i - 1][1])
      dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + energyDrinkB[i])

    return max(dp[-1])
