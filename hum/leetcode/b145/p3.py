from heapq import heappop, heappush
from math import inf

M = 10 ** 5
pr = [1] * M
pr[0] = pr[1] = 0
for i in range(2, M):
  if pr[i] == 1:
    for j in range(i + i, M, i):
      pr[j] = 0


class Solution:
  def minOperations(self, n: int, m: int) -> int:

    length = len(str(n))
    p10 = [1]
    for i in range(1, length):
      p10.append(p10[-1] * 10)

    def dijkstra(src):
      dist = [inf] * M
      vis = [False] * M
      hpq = [(n, src)]
      dist[src] = n

      while hpq:
        d, u = heappop(hpq)
        if vis[u]:
          continue
        vis[u] = True
        sn = str(u)
        for i in range(len(sn)):
          if sn[i] != '9':
            cur = u + p10[len(sn) - 1 - i]
            if not pr[cur]:
              if dist[cur] > d + cur:
                dist[cur] = d + cur
              heappush(hpq, (dist[cur], cur))

          if sn[i] != '0':
            cur = u - p10[len(sn) - 1 - i]
            if not pr[cur]:
              if dist[cur] > d + cur:
                dist[cur] = d + cur
              heappush(hpq, (dist[cur], cur))
      return dist

    if pr[n]:
      return -1
    dist = dijkstra(n)
    return -1 if dist[m] == inf else dist[m]


s = Solution()
print(s.minOperations(n=10, m=12))
