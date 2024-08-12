from typing import List


class Solution:
  def countGoodNodes(self, edges: List[List[int]]) -> int:
    n = len(edges) + 1
    graph = [[] for _ in range(n)]
    for a, b in edges:
      graph[a].append(b)
      graph[b].append(a)
    s = [0] * n
    ans = 0

    def dfs(u, p):
      nonlocal ans
      se = set()
      s[u] = 1
      for v in graph[u]:
        if v == p: continue
        dfs(v, u)
        se.add(s[v])
        s[u] += s[v]

      if len(se) <= 1:
        ans += 1

    dfs(0, 0)
    return ans
