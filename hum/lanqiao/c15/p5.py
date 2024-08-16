import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = input()
graph = [[] for _ in range(n)]
for _ in range(n - 1):
  x, y = map(lambda x: int(x) - 1, input().split())
  graph[x].append(y)
  graph[y].append(x)

mod = 998244353

dfs_order = []
parent = [-1] * n
dep = [0] * n
stack = [0]
dep[0] = 1
cnt = [[0] * 2 for _ in range(n)]
while stack:
  u = stack.pop()
  cnt[u][int(a[u])] += 1
  dfs_order.append(u)
  for v in graph[u]:
    if v == parent[u]:
      continue
    parent[v] = u
    dep[v] = dep[u] + 1
    stack.append(v)
res = 0
for u in reversed(dfs_order):
  if u:
    res = (res + (cnt[parent[u]][0] * cnt[u][1] * dep[parent[u]])) % mod
    res = (res + (cnt[parent[u]][1] * cnt[u][0] * dep[parent[u]])) % mod
    cnt[parent[u]][0] += cnt[u][0]
    cnt[parent[u]][1] += cnt[u][1]

print(res)
