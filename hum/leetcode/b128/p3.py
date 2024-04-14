from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
  def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
    graph = [[] for _ in range(n)]
    for u, v, l in edges:
      graph[u].append((v, l))
      graph[v].append((u, l))

    def dijkstra(graph, src):
      n = len(graph)
      dist = [inf] * n
      vis = [False] * n
      hpq = [(0, src)]
      dist[src] = 0

      while hpq:
        d, u = heappop(hpq)
        if vis[u]:
          continue
        vis[u] = True

        for v, w in graph[u]:
          if dist[v] > d + w and disappear[v] > d + w:
            dist[v] = d + w
            heappush(hpq, (dist[v], v))

      return dist

    res = dijkstra(graph, 0)
    return [-1 if x == inf else x for x in res]
