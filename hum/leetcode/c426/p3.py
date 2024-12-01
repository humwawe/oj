from typing import List


class Solution:
  def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
    n, m = len(edges1) + 1, len(edges2) + 1
    graph1 = [[] for _ in range(n)]
    graph2 = [[] for _ in range(m)]
    for u, v in edges1:
      graph1[u].append(v)
      graph1[v].append(u)
    for u, v in edges2:
      graph2[u].append(v)
      graph2[v].append(u)

    def bfs(graph, s):
      d = [-1] * len(graph)
      d[s] = 0
      stack = [s]
      while stack:
        u = stack.pop()
        for v in graph[u]:
          if d[v] == -1:
            d[v] = d[u] + 1
            stack.append(v)
      return d

    c = 0
    for i in range(m):
      dist = bfs(graph2, i)
      c = max(c, sum(1 if dist[j] <= k - 1 else 0 for j in range(m)))

    res = [0] * n
    for i in range(n):
      dist = bfs(graph1, i)
      res[i] = sum(1 if dist[j] <= k else 0 for j in range(n)) + c

    return res
