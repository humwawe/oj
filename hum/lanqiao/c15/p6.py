n, k = map(int, input().split())
a = list(map(int, input().split()))
b, c, d = [], [], []
for i in range(n):
  if a[i] <= k:
    b.append(a[i])
  else:
    if a[i] % 2 == 0:
      c.append(a[i])
    else:
      d.append(a[i])

b.sort(reverse=True)

res = 0
for i in range(0, len(b), 2):
  res += b[i]

for i in range(len(c)):
  res += c[i] // 2

d.sort(reverse=True)
f = (len(b) + len(c)) % 2
for i in range(len(d)):
  if f == 0:
    res += d[i] // 2
  else:
    res += (d[i] + 1) // 2
  f = 1 - f

print(res)
