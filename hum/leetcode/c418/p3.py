from typing import List


class Solution:
  def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    g = [[] for _ in range(n)]
    for x, y in edges:
      g[x].append(y)
      g[y].append(x)

    # 每种度数选一个点
    deg_to_node = [-1] * 5
    for x, e in enumerate(g):
      deg_to_node[len(e)] = x

    if deg_to_node[1] != -1:
      # 答案只有一列
      row = [deg_to_node[1]]
    elif deg_to_node[4] == -1:
      # 答案只有两列
      x = deg_to_node[2]
      for y in g[x]:
        if len(g[y]) == 2:
          row = [x, y]
          break
    else:
      # 答案至少有三列
      x = deg_to_node[2]
      row = [x]
      pre = x
      x = g[x][0]
      while len(g[x]) > 2:
        row.append(x)
        for y in g[x]:
          if y != pre and len(g[y]) < 4:
            pre = x
            x = y
            break
      row.append(x)

    res = [[] for _ in range(n // len(row))]
    res[0] = row
    vis = [False] * n
    for x in row:
      vis[x] = True
    for i in range(1, len(res)):
      for x in res[i - 1]:
        for y in g[x]:
          # x 上左右的邻居都访问过了，没访问过的邻居只会在 x 下面
          if not vis[y]:
            vis[y] = True
            res[i].append(y)
            break
    return res
