n, k = map(int, input().split())
a = list(map(int, input().split()))

if k % 2 == 0:
  res = 0
  for i in range(1, k, 2):
    res += a[i] - a[i - 1]
  print(res)
else:
  tmp = 0
  for i in range(2, k, 2):
    tmp += a[i] - a[i - 1]
  res = tmp

  for i in range(1, k):
    if i % 2 == 1:
      tmp -= a[i + 1] - a[i]
      tmp += a[i + 1] - a[i - 1]
    else:
      tmp -= a[i] - a[i - 2]
      tmp += a[i - 1] - a[i - 2]

    res = min(res, tmp)

  print(res)
