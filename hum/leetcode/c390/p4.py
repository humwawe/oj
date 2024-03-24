from typing import List


class Trie:

  def __init__(self):
    self.sons = {}
    self.val = (10 ** 18, 10 ** 18)

  def insert(self, word, value):
    rt = self
    for c in word:
      if value < rt.val:
        rt.val = value
      if c not in rt.sons:
        rt.sons[c] = Trie()
      rt = rt.sons[c]

    if value < rt.val:
      rt.val = value

  def search(self, word):
    rt = self
    for c in word:
      if c not in rt.sons:
        break
      rt = rt.sons[c]

    return rt.val[1]


class Solution:
  def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
    root = Trie()
    for i, w in enumerate(wordsContainer):
      root.insert(w[::-1], (len(w), i))

    res = []
    for w in wordsQuery:
      res.append(root.search(w[::-1]))

    return res


s = Solution()
print(s.stringIndices(wordsContainer=["bcd", "xbcd"], wordsQuery=["xyz"]))
