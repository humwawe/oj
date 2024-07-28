from functools import cache
from itertools import accumulate
from typing import List


class Solution:
  def maximumScore(self, grid: List[List[int]]) -> int:
    n = len(grid)

    # 预计算每列的前缀和
    col_sum_list = [list(accumulate(col, initial=0)) for col in zip(*grid)]

    # 辅助函数，用于计算col_index列从[start, end]之间的和
    def col_sum(col_index: int, start: int, end: int) -> int:
      if col_index < 0 or col_index >= n or end < start:
        return 0
      return col_sum_list[col_index][end] - col_sum_list[col_index][start - 1]

    # [前一个峰高度, 当前所在列, 前一列状况(空一列， 空两列， 上， 下）]
    @cache
    def dfs(prev_height: int, curr_col: int, pattern: int) -> int:
      # 结束条件
      if curr_col == n:
        return 0

      max_score = 0

      if pattern == 0:  # 前一个位置是空的
        # 当前列继续空着
        max_score = dfs(0, curr_col + 1, 1)

        # 当前列涂黑前row行
        for row in range(1, n):
          max_score = max(max_score, col_sum(curr_col - 1, prev_height + 1, row) + dfs(row, curr_col + 1, 2))

        # 当前列全部涂黑
        max_score = max(max_score,
                        col_sum(curr_col - 1, prev_height + 1, n) + col_sum(curr_col + 1, 1, n) + dfs(n, curr_col + 1,
                                                                                                      3))

      elif pattern == 1:  # 前两个位置是空的
        # 当前列涂黑前row行
        for row in range(1, n):
          max_score = max(max_score, col_sum(curr_col - 1, 1, row) + dfs(row, curr_col + 1, 2))
        # 当前列全部涂黑
        max_score = max(max_score, col_sum(curr_col - 1, 1, n) + col_sum(curr_col + 1, 1, n) + dfs(n, curr_col + 1, 3))

      elif pattern == 2:  # 前一个位置在上升
        # 当前列涂黑前row行，保持上升
        for row in range(prev_height, n):
          max_score = max(max_score, col_sum(curr_col - 1, prev_height + 1, row) + dfs(row, curr_col + 1, 2))
        # 当前列全部涂黑
        max_score = max(max_score,
                        col_sum(curr_col - 1, prev_height + 1, n) + col_sum(curr_col + 1, 1, n) + dfs(n, curr_col + 1,
                                                                                                      3))

      elif pattern == 3:  # 前一个位置在下降
        # 当前列涂黑前row行，保持下降
        for row in range(1, prev_height + 1):
          max_score = max(max_score,
                          col_sum(curr_col + 1, 1, row) - col_sum(curr_col, 1, row) + dfs(row, curr_col + 1, 3))
        # 不涂当前列
        max_score = max(max_score, dfs(prev_height, curr_col + 1, 0))
      return max_score

    return dfs(0, 0, 0)
