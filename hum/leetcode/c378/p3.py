from collections import defaultdict, Counter


class Solution:
  def maximumLength(self, s: str) -> int:
    n = len(s)
    tmp = defaultdict(list)
    for i in range(n):
      tmp[s[i]].append(i)
    res = -1
    for k in tmp:
      cur = tmp[k]
      cnt = Counter()
      i = 0
      while i < len(cur):
        j = i
        while j + 1 < len(cur) and cur[j + 1] == cur[j] + 1:
          j += 1
        cnt[j - i + 1] += 1
        i = j + 1
      max_len = max(cnt.keys())

      if cnt[max_len] >= 3:
        res = max(res, max_len)
      cnt[max_len - 1] += cnt[max_len] * 2
      max_len -= 1
      if max_len != 0 and cnt[max_len] >= 3:
        res = max(res, max_len)

      cnt[max_len - 1] += cnt[max_len] * 2
      max_len -= 1
      if max_len != 0 and cnt[max_len] >= 3:
        res = max(res, max_len)

    return res
