from typing import List


class Solution:
  def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

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

    d = bfs(graph1, 0)
    st = [0] * n
    c1 = 0
    c2 = 0
    for i in range(n):
      if d[i] % 2 == 0:
        c1 += 1
      else:
        c2 += 1
        st[i] = 1

    d = bfs(graph2, 0)
    t = sum(1 if d[j] % 2 == 1 else 0 for j in range(m))
    c = max(t, m - t)

    res = [0] * n
    for i in range(n):
      res[i] = (c1 if st[i] == 0 else c2) + c

    return res
