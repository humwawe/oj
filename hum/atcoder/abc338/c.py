n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def work():
  inf = float("inf")
  cnt = inf
  for i in range(n):
    if tmp[i] < 0:
      return -inf
    if b[i] == 0:
      continue
    cnt = min(cnt, tmp[i] // b[i])

  return cnt if cnt != inf else -inf


res = 0
for i in range(max(q) + 1):
  tmp = [q[j] - a[j] * i for j in range(n)]
  res = max(res, i + work())

print(res)
