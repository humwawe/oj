from collections import defaultdict


class Solution:
  def countOfSubstrings(self, word: str, k: int) -> int:
    n = len(word)
    cnt = defaultdict(int)
    cnt1 = 0
    cnt2 = 0
    s = set("aeiou")
    j = 0

    right = [0] * n
    for i in range(n - 2, -1, -1):
      if word[i + 1] in s:
        right[i] = right[i + 1] + 1

    res = 0

    for i in range(n):
      while j < n and (cnt1 < 5 or cnt2 < k):
        c = word[j]
        if c in s:
          cnt[c] += 1
          if cnt[c] == 1:
            cnt1 += 1
        else:
          cnt2 += 1
        j += 1

      if cnt1 == 5 and cnt2 == k:
        res += right[j - 1] + 1

      c = word[i]
      if c in s:
        cnt[c] -= 1
        if cnt[c] == 0:
          cnt1 -= 1
      else:
        cnt2 -= 1
    return res
