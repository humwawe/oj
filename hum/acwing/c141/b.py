n = int(input())
a = list(map(int, input().split()))

for i in range(n):
  x, y = divmod(a[i], n)
  a[i] = x * n + (n + i if y > i else i)

print(a.index(min(a)) + 1)
