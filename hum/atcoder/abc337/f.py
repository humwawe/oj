from collections import Counter

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
f = Counter(a)
a += a
r = 0

cnt = Counter()
res = 0
now = 0
for l in range(n):
  while r < n + l and now < m:
    cnt[a[r]] += 1
    if (cnt[a[r]] - 1) % k == 0:
      now += 1
      res += min(f[a[r]] - (cnt[a[r]] - 1), k)
    r += 1

  print(res)
  cnt[a[l]] -= 1
  if cnt[a[l]] % k == 0:
    now -= 1
    res -= min(f[a[l]] - cnt[a[l]], k)
