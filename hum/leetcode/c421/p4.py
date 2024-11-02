from typing import List


def matrix_mul(A, B, mod=10 ** 9 + 7):
  n, m = len(A), len(A[0])
  p = len(B[0])
  ans = [[0] * p for _ in range(n)]
  for i in range(n):
    for j in range(m):
      for k in range(p):
        ans[i][k] += A[i][j] * B[j][k]
        ans[i][k] %= mod
  return ans


def matrix_pow(x, n):
  if n == 0:
    k = len(x)
    grid = [[0] * k for _ in range(k)]
    for i in range(k):
      grid[i][i] = 1
    return grid
  if n == 1: return x
  if n == 2: return matrix_mul(x, x)
  v = matrix_pow(x, n // 2)
  ans = matrix_mul(v, v)
  if n % 2 == 0:
    return ans
  return matrix_mul(ans, x)


class Solution:
  def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
    grid = [[0] * 26 for _ in range(26)]
    for i in range(26):
      for j in range(1, nums[i] + 1):
        grid[i][(i + j) % 26] = 1
    cnt = [[0] * 26]
    for c in s:
      cnt[0][ord(c) - ord('a')] += 1
    return sum(matrix_mul(cnt, matrix_pow(grid, t))[0]) % (10 ** 9 + 7)
