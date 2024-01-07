from collections import deque


class Solution:
  def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
    if x <= y:
      return y - x
    lim = x * 11 + 5
    dis = [-1] * lim
    dis[x] = 0
    q = deque([x])
    while q:
      cur = q.popleft()
      if cur % 11 == 0 and dis[cur // 11] == -1:
        dis[cur // 11] = dis[cur] + 1
        q.append(cur // 11)
      if cur % 5 == 0 and dis[cur // 5] == -1:
        dis[cur // 5] = dis[cur] + 1
        q.append(cur // 5)
      if cur + 1 < lim and dis[cur + 1] == -1:
        dis[cur + 1] = dis[cur] + 1
        q.append(cur + 1)
      if cur - 1 >= 0 and dis[cur - 1] == -1:
        dis[cur - 1] = dis[cur] + 1
        q.append(cur - 1)

    return dis[y]
