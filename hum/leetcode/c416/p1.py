from typing import List


class Solution:
  def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
    bw = set(bannedWords)
    cnt = 0
    for m in message:
      if m in bw:
        cnt += 1
    return cnt >= 2
