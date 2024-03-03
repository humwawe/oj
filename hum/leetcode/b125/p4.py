from typing import List


class Solution:
  def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
    graph = [[] for _ in nums]
    for x, y in edges:
      graph[x].append(y)
      graph[y].append(x)
    dp = [[0, -float('inf')] for _ in range(len(nums) + 1)]

    def dfs(u, p):
      for v in graph[u]:
        if v == p:
          continue
        dfs(v, u)
        dp[u][0], dp[u][1] = max(dp[u][0] + dp[v][0], dp[u][1] + dp[v][1]), max(dp[u][1] + dp[v][0],
                                                                                dp[u][0] + dp[v][1])
      dp[u][0], dp[u][1] = max(dp[u][0] + nums[u], dp[u][1] + (nums[u] ^ k)), max(dp[u][1] + nums[u],
                                                                                  dp[u][0] + (nums[u] ^ k))

    dfs(0, 0)
    return dp[0][0]
