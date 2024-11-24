from typing import List


class Solution:
  def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
    n = len(edges) + 1
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
      graph[u].append((v, w))
      graph[v].append((u, w))

    def dfs(u, p):
      t = []
      for v, w in graph[u]:
        if v == p:
          continue
        t1, t2 = dfs(v, u)
        t.append((t1 + w, t2, t1 + w - t2))
      t.sort(key=lambda x: x[2], reverse=True)
      res1 = 0
      res2 = 0
      for i in range(len(t)):
        if i < k - 1:
          res1 += max(t[i][0], t[i][1])
        else:
          res1 += t[i][1]

        if i < k:
          res2 += max(t[i][0], t[i][1])
        else:
          res2 += t[i][1]

      print(u, res1, res2)
      return res1, res2

    return max(dfs(0, -1))
