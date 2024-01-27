n = int(input())
a = list(map(int, input().split()))
pre = [1] * n
suf = [1] * n
for i in range(1, n):
  pre[i] = min(pre[i - 1] + 1, a[i])
for i in range(n - 2, -1, -1):
  suf[i] = min(suf[i + 1] + 1, a[i])

print(max([min(pre[i], suf[i]) for i in range(n)]))
