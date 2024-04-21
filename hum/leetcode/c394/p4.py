from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
  def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
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
          if dist[v] > d + w:
            dist[v] = d + w
            heappush(hpq, (dist[v], v))

      return dist

    graph = [[] for _ in range(n)]
    for x, y, w in edges:
      graph[x].append((y, w))
      graph[y].append((x, w))

    dist_s = dijkstra(graph, 0)
    d = dist_s[n - 1]
    print(d)
    dist_t = dijkstra(graph, n - 1)

    res = []
    for x, y, w in edges:
      if d == inf:
        res.append(False)
        continue
      if dist_s[x] + dist_t[y] + w == d or dist_s[y] + dist_t[x] + w == d:
        res.append(True)
      else:
        res.append(False)
    return res


s = Solution()
print(s.findAnswer(3, [[2, 1, 6]]))
