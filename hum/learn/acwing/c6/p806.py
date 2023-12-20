def add(x, y):
  return x + y


x, y = map(float, input().split())
print(f"{add(x, y):.2f}")
