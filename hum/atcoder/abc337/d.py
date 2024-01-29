h, w, k = map(int, input().split())

a = []
for _ in range(h):
  a.append(input())

res = float('inf')


def work():
  global res
  tmp = []
  cnt = 0
  for x in cur:
    if x == 'x':
      tmp.clear()
      cnt = 0
    elif x == '.':
      tmp.append(0)
    else:
      tmp.append(1)
      cnt += 1

    if len(tmp) > k:
      cnt -= tmp[-k - 1]
    if len(tmp) >= k:
      res = min(res, k - cnt)


for i in range(h):
  cur = a[i]
  work()

for i in range(w):
  cur = ''.join([a[j][i] for j in range(h)])
  work()

print(-1 if res == float('inf') else res)
