from typing import List


class Solution:
  def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
    n, m = len(edges1) + 1, len(edges2) + 1
    g1 = [[] for _ in range(n)]
    for u, v in edges1:
      g1[u].append(v)
      g1[v].append(u)
    g2 = [[] for _ in range(m)]
    for u, v in edges2:
      g2[u].append(v)
      g2[v].append(u)

    def f(n, g):
      dfs_order = []
      p = [-1] * n
      stack = [0]
      while stack:
        u = stack.pop()
        dfs_order.append(u)
        for v in g[u]:
          if p[u] == v:
            continue
          p[v] = u
          stack.append(v)
      dep = [0] * n
      l = 0
      for u in reversed(dfs_order):
        for v in g[u]:
          if p[u] == v:
            continue
          l = max(l, dep[u] + dep[v] + 1)
          dep[u] = max(dep[u], dep[v] + 1)
      return l

    l1 = f(n, g1)
    l2 = f(m, g2)

    return max(l1, l2, (l1 + 1) // 2 + (l2 + 1) // 2 + 1)
