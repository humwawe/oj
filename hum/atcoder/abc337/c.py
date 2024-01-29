n = int(input())
a = list(map(int, input().split()))
ma = [-1] * (n + 1)
res = []
for i in range(n):
  if a[i] == -1:
    res.append(i + 1)
    continue
  ma[a[i]] = i + 1

while ma[res[-1]] != -1:
  res.append(ma[res[-1]])

print(*res)
