from collections import Counter
from string import ascii_lowercase


class Solution:
  def makeStringGood(self, s: str) -> int:
    cnt = Counter(s)
    cnt = [cnt[c] for c in ascii_lowercase]

    ans = len(s)
    f = [0] * 27
    for target in range(max(cnt) + 1):
      f[25] = min(cnt[25], abs(cnt[25] - target))
      for i in range(24, -1, -1):
        x, y = cnt[i], cnt[i + 1]
        f[i] = f[i + 1] + min(x, abs(x - target))
        if y < target:
          t = target if x > target else 0
          f[i] = min(f[i], f[i + 2] + max(x - t, target - y))
      ans = min(ans, f[0])
    return ans
