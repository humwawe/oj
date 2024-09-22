class Solution:
  def validSubstringCount(self, word1: str, word2: str) -> int:
    n = len(word1)
    cnt2 = [0] * 26
    cnt1 = [0] * 26
    word1 = [ord(c) - ord('a') for c in word1]

    for c in word2:
      cnt2[ord(c) - ord('a')] += 1

    st = 0

    for i in range(26):
      if cnt1[i] < cnt2[i]:
        st |= (1 << i)

    def check(cnt1, c):
      nonlocal st
      cnt1[c] += 1
      if cnt1[c] >= cnt2[c]:
        st &= ~(1 << c)
      res = (st != 0)
      cnt1[c] -= 1
      return res

    l = 0
    r = -1
    res = 0
    while l < n:
      while r + 1 < n and check(cnt1, word1[r + 1]):
        r += 1
        cnt1[word1[r]] += 1
      res += n - (r + 1)
      cnt1[word1[l]] -= 1
      if cnt1[word1[l]] < cnt2[word1[l]]:
        st |= 1 << word1[l]

      l += 1
    return res
