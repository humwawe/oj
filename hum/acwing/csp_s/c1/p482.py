n = int(input())
a = list(map(int, input().split()))

pre = [1] * n
for i in range(n):
  for j in range(0, i):
    if a[j] < a[i]:
      pre[i] = max(pre[i], pre[j] + 1)

suf = [1] * n
for i in range(n - 1, -1, -1):
  for j in range(n - 1, i, -1):
    if a[j] < a[i]:
      suf[i] = max(suf[i], suf[j] + 1)

res = n - 1
for i in range(n):
  res = min(res, n - (pre[i] + suf[i] - 1))

print(res)