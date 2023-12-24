from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List


class Dijkstra:
  def dijkstra(self, graph, src):
    dis = defaultdict(lambda: inf)
    vis = set()
    hpq = [(0, src)]
    dis[src] = 0

    while hpq:
      d, u = heappop(hpq)
      if u in vis:
        continue
      vis.add(u)

      for v in graph[u]:
        if dis[v] > d + graph[u][v]:
          dis[v] = d + graph[u][v]
          heappush(hpq, (dis[v], v))

    return dis


class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    path = defaultdict(lambda: defaultdict(lambda: inf))
    for x, y, z in zip(original, changed, cost):
      path[x][y] = min(path[x][y], z)

    dist = defaultdict()
    dij = Dijkstra()

    for x in original:
      dist[x] = dij.dijkstra(path, x)
    print(path.keys())
    print(1111)
    n = len(source)
    dp = [inf for _ in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
      if source[i - 1] == target[i - 1]:
        dp[i] = dp[i - 1]
      for key in original:
        tmp = source[i - len(key):i]
        if tmp == key and i - len(key) >= 0 and target[i - len(key):i] in dist[tmp]:
          dp[i] = min(dp[i], dp[i - len(key)] + dist[tmp][target[i - len(key):i]])

    return dp[-1] if dp[-1] < inf else -1
