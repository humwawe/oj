import random
from typing import List


class StringHash:
  def __init__(self, s, mod):
    self.N = len(s)
    self.BASE = 131  # random.randint(100, 500)
    self.MOD = mod
    self.h = h = [0] * (self.N + 1)
    self.p = p = [1] * (self.N + 1)
    for i in range(1, self.N + 1):
      p[i] = (p[i - 1] * self.BASE) % self.MOD
      h[i] = (h[i - 1] * self.BASE + ord(s[i - 1])) % self.MOD

  # [l,r)
  def __get_hash(self, l, r):
    return (self.h[r] - self.h[l] * self.p[r - l]) % self.MOD

  def __getitem__(self, item) -> int:
    if isinstance(item, int):
      return (self.h[item + 1] - self.h[item] * self.p[1]) % self.MOD
    else:
      l, r = item.start, item.stop
      if l is None:
        l = 0
      if r is None:
        r = self.N
      return self.__get_hash(l, r)


class Solution:
  def findAnswer(self, parent: List[int], s: str) -> List[bool]:
    n = len(parent)
    graph = [[] for _ in range(n)]
    for i in range(1, n):
      graph[parent[i]].append(i)
    r = []
    size = [0] * n

    def dfs(u):
      graph[u].sort()
      res = []
      for v in graph[u]:
        res.append(dfs(v))
        size[u] += size[v]

      res.append(s[u])
      r.append(u)

      size[u] += 1
      return ''.join(res)

    dfs_s = dfs(0)
    MOD = random.getrandbits(64)
    shs = StringHash(dfs_s, MOD)
    shs_r = StringHash(dfs_s[::-1], MOD)
    res = [False] * n

    for i in range(n):
      right = i
      left = i - size[r[i]] + 1

      if shs[left: right + 1] == shs_r[n - right - 1: n - left]:
        res[r[i]] = True

    return res


s = Solution()
print(s.findAnswer(parent=[-1, 0, 0, 1, 1, 2], s="aababa"))
