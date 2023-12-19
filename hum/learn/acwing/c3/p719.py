n = int(input())
for _ in range(n):
  x, y = sorted(map(int, input().split()))
  s = 0
  for i in range(x + 1, y):
    if i % 2 == 1:
      s += i
  print(s)
