n = int(input())
a = list(map(int, input().split()))

m = float('inf')
t = 0
for i in a:
  t += i
  m = min(m, t)

print(max(0, -m) + sum(a))
