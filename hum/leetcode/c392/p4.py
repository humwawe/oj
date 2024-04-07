from collections import defaultdict
from typing import List


class Solution:

  def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
    class DJSet:
      def __init__(self, n):
        self.p = [-1] * n

      def find(self, x):
        if self.p[x] < 0:
          return x
        nx = x
        while self.p[x] >= 0:
          x = self.p[x]
        while nx != x:
          self.p[nx], nx = x, self.p[nx]
        return x

      def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
          if self.p[y] < self.p[x]:
            x, y = y, x
          self.p[x] += self.p[y]
          self.p[y] = x
        return x == y

      def equiv(self, x, y):
        return self.find(x) == self.find(y)

      def count(self):
        cnt = 0
        for i in self.p:
          if i < 0:
            cnt += 1
        return cnt

      def size(self, x):
        return -self.p[self.find(x)]

      def to_bucket(self):
        n = len(self.p)
        ret = [[] for _ in range(n)]
        for i in range(n):
          r = self.find(i)
          ret[r].append(i)
        return ret

    djset = DJSet(n)
    for a, b, c in edges:
      djset.merge(a, b)
    tmp = defaultdict(lambda: -1)

    for a, b, c in edges:
      if (r := djset.find(a)) == djset.find(b):
        tmp[r] &= c

    res = []
    for a, b in query:
      if a == b:
        res.append(0)
      elif (r := djset.find(a)) == djset.find(b):
        res.append(tmp[r])
      else:
        res.append(-1)

    return res
