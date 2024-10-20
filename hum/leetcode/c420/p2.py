class Solution:
  def numberOfSubstrings(self, s: str, k: int) -> int:
    n = len(s)
    s = [ord(x) - ord('a') for x in s]
    cnt = [0] * 26
    j = -1
    res = n * (n + 1) // 2
    for i in range(n):
      while j + 1 < n and cnt[s[j + 1]] + 1 < k:
        j += 1
        cnt[s[j]] += 1
      res -= j - i + 1
      cnt[s[i]] -= 1

    return res
