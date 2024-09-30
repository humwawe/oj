class Solution:
  def kthCharacter(self, k: int) -> str:
    word = [0]
    while len(word) < k:
      t = len(word)
      for i in range(t):
        word.append((word[i] + 1) % 26)
    return chr(ord('a') + word[k - 1])
