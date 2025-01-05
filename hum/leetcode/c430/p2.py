class Solution:
  def answerString(self, word: str, numFriends: int) -> str:
    n = len(word)
    if numFriends == 1:
      return word
    cur = ""
    length = n - numFriends + 1
    for i in range(n):
      if word[i:min(i + length, n)] > cur:
        cur = word[i:min(i + length, n)]
    return cur
