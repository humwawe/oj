from typing import List


class Solution:
  def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(n)]
    for a, b in invocations:
      graph[a].append(b)

    inv = set()

    def dfs(u):
      if u in inv:
        return
      inv.add(u)
      for v in graph[u]:
        dfs(v)

    dfs(k)

    for u in range(n):
      for v in graph[u]:
        if v in inv and u not in inv:
          return list(range(n))

    res = set(range(n)).difference(inv)
    return list(res)
