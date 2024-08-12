from typing import List

from sortedcontainers import SortedList


class FenwickTree:
  def __init__(self, n: int):
    self.t = [[0, 0] for _ in range(n + 1)]

  # op=1，添加一个 size
  # op=-1，移除一个 size
  def update(self, size: int, op: int) -> None:
    i = len(self.t) - size
    while i < len(self.t):
      self.t[i][0] += op
      self.t[i][1] += op * size
      i += i & -i

  # 返回 >= size 的元素个数，元素和
  def query(self, size: int) -> (int, int):
    cnt = s = 0
    i = len(self.t) - size
    while i > 0:
      cnt += self.t[i][0]
      s += self.t[i][1]
      i &= i - 1
    return cnt, s


class Solution:
  def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
    n = len(colors)
    sl = SortedList()
    t = FenwickTree(n)

    # op=1，添加一个结束位置 i
    # op=-1，移除一个结束位置 i
    def update(i: int, op: int) -> None:
      idx = sl.bisect_left(i)
      pre = sl[idx - 1]
      nxt = sl[idx % len(sl)]

      t.update((nxt - pre - 1) % n + 1, -op)  # 移除/添加旧长度
      t.update((i - pre) % n, op)
      t.update((nxt - i) % n, op)  # 添加/移除新长度

    # 添加一个结束位置 i
    def add(i: int) -> None:
      if not sl:
        t.update(n, 1)
      else:
        update(i, 1)
      sl.add(i)

    # 移除一个结束位置 i
    def remove(i: int) -> None:
      sl.remove(i)
      if not sl:
        t.update(n, -1)
      else:
        update(i, -1)

    for i, c in enumerate(colors):
      if c == colors[(i + 1) % n]:
        add(i)  # i 是一个结束位置

    res = []
    for q in queries:
      if q[0] == 1:
        if not sl:
          res.append(n)  # 每个长为 size 的子数组都符合要求
        else:
          cnt, s = t.query(q[1])
          res.append(s - cnt * (q[1] - 1))
      else:
        i, c = q[1], q[2]
        if colors[i] == c:  # 无影响
          continue
        pre, nxt = (i - 1) % n, (i + 1) % n
        # 修改前，先去掉结束位置
        if colors[pre] == colors[i]:
          remove(pre)
        if colors[i] == colors[nxt]:
          remove(i)
        colors[i] = c
        # 修改后，添加新的结束位置
        if colors[pre] == colors[i]:
          add(pre)
        if colors[i] == colors[nxt]:
          add(i)
    return res
