n, x, y = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


def dfs(x):
  stack = [x]
  dfs_order = []
  parent = [-1] * (n + 1)
  while stack:
    u = stack.pop()
    dfs_order.append(u)
    for v in graph[u]:
      if parent[u] != v:
        parent[v] = u
        stack.append(v)
  dfs_order.reverse()
  return dfs_order


sz = [0] * (n + 1)
dfs_order = dfs(x)
for u in dfs_order:
  sz[u] = 1
  for v in graph[u]:
    sz[u] += sz[v]
r1 = sz[y]

sz = [0] * (n + 1)
dfs_order = dfs(y)
for u in dfs_order:
  sz[u] = 1
  for v in graph[u]:
    sz[u] += sz[v]
r2 = sz[x]

print(n * (n - 1) - r1 * r2)
