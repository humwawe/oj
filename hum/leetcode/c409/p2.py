from collections import deque
from typing import List


class Solution:
  def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
      graph[i].append(i + 1)

    def bfs():
      dis = [1000] * n
      q = deque([0])
      dis[0] = 0
      while q:
        u = q.popleft()
        for v in graph[u]:
          if dis[v] == 1000:
            dis[v] = dis[u] + 1
            q.append(v)
      return dis[-1]

    res = []
    for a, b in queries:
      graph[a].append(b)
      res.append(bfs())
    return res
