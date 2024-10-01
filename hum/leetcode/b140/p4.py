class Solution:
  def minStartingIndex(self, s: str, pattern: str) -> int:

    def z_function(s):
      n = len(s)
      z = [0] * n
      l, r = 0, 0
      for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
          z[i] = z[i - l]
        else:
          z[i] = max(0, r - i + 1)
          while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
          l = i
          r = i + z[i] - 1
      return z

    n, m = len(s), len(pattern)

    res1 = z_function(pattern + "#" + s)[m + 1:]
    res2 = z_function(pattern[::-1] + "#" + s[::-1])[m + 1:]
    res2.reverse()

    for i in range(n - m + 1):
      l, r = i, i + m - 1
      if res1[l] + res2[r] + 1 >= m:
        return i
    return -1
