from heapq import heappop, heappush, nlargest
from typing import List


class Solution:
  def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
    n = len(cost)
    g = [[] for _ in range(n)]
    for edge in edges:
      g[edge[0]].append(edge[1])
      g[edge[1]].append(edge[0])
    tmp1 = [[] for _ in range(n)]
    tmp2 = [[] for _ in range(n)]

    res = [0] * n
    size = [0] * n

    def dfs(u: int, p: int):
      size[u] += 1
      if cost[u] >= 0:
        tmp1[u].append(cost[u])
      else:
        tmp2[u].append(-cost[u])

      for v in g[u]:
        if v == p:
          continue
        dfs(v, u)
        size[u] += size[v]

        for i in tmp1[v]:
          heappush(tmp1[u], i)
        for i in tmp2[v]:
          heappush(tmp2[u], i)
        while len(tmp1[u]) > 3:
          heappop(tmp1[u])
        while len(tmp2[u]) > 2:
          heappop(tmp2[u])

      if size[u] < 3:
        res[u] = 1
      else:
        if len(tmp1[u]) >= 3:
          res[u] = max(res[u], tmp1[u][0] * tmp1[u][1] * tmp1[u][2])
        if len(tmp2[u]) >= 2 and len(tmp1[u]) >= 1:
          res[u] = max(res[u], nlargest(1, tmp1[u])[0] * tmp2[u][0] * tmp2[u][1])

    dfs(0, 0)

    return res
