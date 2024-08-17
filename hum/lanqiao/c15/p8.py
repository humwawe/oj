from itertools import accumulate

n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))

graph = [[] for _ in range(n)]
r = 0
p = [-1] * n
for i in range(n):
  if a[i] == -1:
    r = i
  else:
    graph[a[i]].append(i)
    p[i] = a[i]

stack = [r]
dep = [0] * n
dfs_order = []
while stack:
  u = stack.pop()
  dfs_order.append(u)
  for v in graph[u]:
    dep[v] = dep[u] + 1
    stack.append(v)

size = [1] * n
for u in reversed(dfs_order):
  if p[u] != -1:
    size[p[u]] += size[u]

diff = [0] * (n + 1)

for i in range(n):
  l = dep[i]
  r = n - size[i]
  diff[l] += 1
  diff[r + 1] -= 1

acc = list(accumulate(diff))
acc.pop()
print(*acc)
