class Solution:
  def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
    r1 = ord(coordinate1[0]) - ord('a')
    c1 = int(coordinate1[1]) - 1
    r2 = ord(coordinate2[0]) - ord('a')
    c2 = int(coordinate2[1]) - 1

    if (r1 + c1) % 2 == (r2 + c2) % 2:
      return True
    return False
