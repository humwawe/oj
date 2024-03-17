import heapq
from collections import Counter


class Solution:
  def minimizeStringValue(self, s: str) -> str:
    cnt_q = s.count('?')
    cnt = Counter((c for c in s if c != '?'))
    h = []
    for i in range(26):
      c = chr(ord('a') + i)
      h.append((cnt[c], c))

    heapq.heapify(h)

    while cnt_q > 0:
      num, c = heapq.heappop(h)
      num += 1
      cnt_q -= 1
      heapq.heappush(h, (num, c))

    d = dict()
    while h:
      num, c = h.pop()
      d[c] = num
      d[c] -= cnt[c]

    res = []

    for c in s:
      if c == '?':
        for i in range(26):
          tmp = chr(ord('a') + i)
          if d[tmp] > 0:
            res.append(tmp)
            d[tmp] -= 1
            break
      else:
        res.append(c)

    return ''.join(res)
