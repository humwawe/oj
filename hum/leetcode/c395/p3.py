class Solution:
  def minEnd(self, n: int, x: int) -> int:
    sx = bin(x)[2:]
    zero = sx.count('0')
    n -= 1

    if n.bit_length() > zero:
      sx = sx.zfill(len(sx) + n.bit_length() - zero)

    sx = list(sx)

    sn = bin(n)[2:][::-1]
    idx = 0
    for i in reversed(range(len(sx))):
      if sx[i] == '0':
        sx[i] = sn[idx]
        idx += 1
        if idx == len(sn):
          break
    return int(''.join(sx), 2)
