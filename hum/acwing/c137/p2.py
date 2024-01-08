n, k, M, D = map(int, input().split())
res = 0
for d in range(1, D + 1):
  x = min(n // ((d - 1) * k + 1), M)
  if x != 0 and (d - 1) * k + 1 <= n // x <= k * d:
    res = max(res, d * x)
print(res)
