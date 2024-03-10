from typing import List


class Solution:
  def shortestSubstrings(self, arr: List[str]) -> List[str]:
    d = dict()
    for word in arr:
      k = len(word)
      for i in range(k):
        for j in range(i, k):
          d[word[i:j + 1]] = d.get(word[i:j + 1], 0) + 1

    res = []
    for word in arr:
      k = len(word)
      for i in range(k):
        for j in range(i, k):
          d[word[i:j + 1]] = d[word[i:j + 1]] - 1

      tmp = ""
      for i in range(k):
        for j in range(i, k):
          if d[word[i:j + 1]] == 0:
            if tmp == "":
              tmp = word[i:j + 1]
            elif j - i + 1 < len(tmp):
              tmp = word[i:j + 1]
            elif j - i + 1 == len(tmp) and tmp > word[i:j + 1]:
              tmp = word[i:j + 1]

      res.append(tmp)

      for i in range(k):
        for j in range(i, k):
          d[word[i:j + 1]] = d[word[i:j + 1]] + 1

    return res
