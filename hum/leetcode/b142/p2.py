from typing import List


class Solution:
  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(s)
    graph = [set() for _ in range(n)]
    ng = [set() for _ in range(n)]
    for i in range(1, n):
      graph[parent[i]].add(i)
      ng[parent[i]].add(i)

    tmp = [[-1] * 26 for _ in range(n)]

    def dfs(u):
      cur = ord(s[u]) - ord('a')
      tmp[u][cur] = u
      for v in graph[u]:
        tmp[v][:] = tmp[u][:]
        dfs(v)
        x = tmp[u][ord(s[v]) - ord('a')]
        if x != -1:
          ng[u].remove(v)
          ng[x].add(v)

    dfs(0)

    res = [1] * n

    def dfs3(u):
      for v in ng[u]:
        dfs3(v)
        res[u] += res[v]

    dfs3(0)

    return res
