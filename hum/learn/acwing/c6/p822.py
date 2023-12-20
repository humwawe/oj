def f(x, y):
  if x < 0 or y < 0:
    return 0
  if x == 0 and y == 0:
    return 1
  return f(x - 1, y) + f(x, y - 1)


n, m = map(int, input().split())
print(f(n, m))
