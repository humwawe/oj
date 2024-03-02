from typing import List


class Solution:
  def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
    n = len(edges) + 1
    graph = [[] for _ in range(n)]
    for edge in edges:
      graph[edge[0]].append((edge[1], edge[2]))
      graph[edge[1]].append((edge[0], edge[2]))

    def dfs(u, p):
      res, prev = 0, 0
      for v, w in graph[u]:
        if v == p:
          continue
        l[v] = l[u] + w
        dfs(v, u)
        if l[v] % signalSpeed == 0:
          s[v] += 1
        res += prev * s[v]
        prev += s[v]
      s[u] = prev
      return res

    res = []
    for i in range(n):
      s = [0] * n
      l = [0] * n
      res.append(dfs(i, i))
    return res


s = Solution()
print(s.countPairsOfConnectableServers(edges=[[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]],
                                       signalSpeed=3))
