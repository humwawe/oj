n = int(input())
d = dict()
root = (0, 0)
for _ in range(n):
  x, y = map(int, input().split())
  if x > y:
    x, y = y, x
  x -= 1
  y -= 1
  d[x] = y

r = [float('inf')]
for i in sorted(d.keys()):
  while i > r[-1]:
    r.pop()
  if d[i] > r[-1]:
    exit(print("Yes"))
  r.append(d[i])

print("No")
