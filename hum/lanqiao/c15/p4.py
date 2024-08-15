n = int(input())
a = list(map(int, input().split()))
m = max(a)
cnt = [[0] * (m + 1) for _ in range(n)]
for i in range(n):
  if i > 0:
    cnt[i] = cnt[i - 1][:]
  cnt[i][a[i]] += 1

res = 0
for c in range(2, n - 2):
  for x in range(1, c):
    if a[c] - a[x] >= 1:
      t1 = cnt[x - 1][a[c] - a[x]]
      if t1 >= 1:
        for y in range(c + 1, n - 1):
          if a[c] - a[y] >= 1:
            t2 = cnt[n - 1][a[c] - a[y]] - cnt[y][a[c] - a[y]]
            res += t1 * t2

print(res)
