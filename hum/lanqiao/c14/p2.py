n = int(input())
a = 1
b = 200
res = 0
for i in range(1, n + 1):
  c, d = map(int, input().split())
  if b * c > a * d:
    a, b = c, d
    res = i

print(res)
