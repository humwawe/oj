from collections import Counter


class Solution:
  def lastNonEmptyString(self, s: str) -> str:
    cnt = Counter(s)
    n = len(s)
    m = max(cnt.values())
    res = []
    for i in range(n - 1, -1, -1):
      if cnt[s[i]] == m:
        res.append(s[i])
        cnt[s[i]] -= 1
    return "".join(reversed(res))
