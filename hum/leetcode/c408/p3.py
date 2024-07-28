from bisect import bisect_left


class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    n = len(s)
    pos = [i for i in range(n) if s[i] == '0']
    pos.append(n)
    m = len(pos)

    res = 0
    for i in range(n):
      j = bisect_left(pos, i)
      res += max(0, pos[j] - i)

      for k in range(j, m - 1):
        cnt0 = k - j + 1
        if cnt0 * cnt0 + cnt0 > n - i:
          break
        p = pos[k]
        q = pos[k + 1]
        cnt1 = p - i + 1 - cnt0
        if cnt1 >= cnt0 * cnt0:
          res += q - p
        else:
          res += max(0, q - (p + cnt0 * cnt0 - cnt1))

    return res


s = Solution()
print(s.numberOfSubstrings("110"))
