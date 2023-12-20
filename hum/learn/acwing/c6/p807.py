def s(a, b):
  res = 0
  for i in range(a, b + 1):
    res += i
  return res


a, b = map(int, input().split())
print(s(a, b))
