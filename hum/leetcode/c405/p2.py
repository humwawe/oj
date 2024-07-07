from typing import List


class Solution:
  def validStrings(self, n: int) -> List[str]:
    res = []

    def dfs(s, x):
      if len(s) == n:
        res.append(s)
        return
      dfs(s + '1', '1')
      if x != '0':
        dfs(s + '0', '0')

    dfs('', '1')

    return res
