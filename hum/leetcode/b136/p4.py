from typing import List


class Solution:
  def timeTaken(self, edges: List[List[int]]) -> List[int]:
    n = len(edges) + 1
    graph = [[] for _ in range(n)]
    for a, b in edges:
      graph[a].append(b)
      graph[b].append(a)

    dis = [[0] * 3 for _ in range(n)]

    def dfs1(u, p):
      for v in graph[u]:
        if v == p:
          continue
        dfs1(v, u)
        t = dis[v][0] + (1 if v % 2 == 1 else 2)
        if t >= dis[u][0]:
          dis[u][0], dis[u][1] = t, dis[u][0]
          dis[u][2] = v
        elif t > dis[u][1]:
          dis[u][1] = t

    dfs1(0, 0)

    dis_up = [0] * n

    def dfs2(u, p):
      for v in graph[u]:
        if v == p:
          continue
        t = 1 if u % 2 == 1 else 2
        dis_up[v] = dis_up[u] + t
        if dis[u][2] == v:
          dis_up[v] = max(dis_up[v], dis[u][1] + t)
        else:
          dis_up[v] = max(dis_up[v], dis[u][0] + t)
        dfs2(v, u)

    dfs2(0, 0)
    res = [0] * n

    for i in range(n):
      res[i] = max(dis_up[i], dis[i][0])
    return res
