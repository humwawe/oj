from collections import Counter

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
tmp = Counter(a)
a += a
r = -1

cnt = Counter()
res = 0
for l in range(n):
  while r - l + 2 <= n and len(cnt) + (a[r + 1] not in cnt) <= m:
    r += 1
    if a[r] not in cnt:
      res += min(tmp[a[r]], k)
    cnt[a[r]] += 1

  print(res)
  if cnt[a[l]] == 1:
    res -= min(tmp[a[l]], k)
    del cnt[a[l]]
  else:
    cnt[a[l]] -= 1
