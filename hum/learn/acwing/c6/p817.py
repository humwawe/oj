def get_unique_count(a, n):
  res = set()
  for i in range(n):
    res.add(a[i])
  return len(res)


n = int(input())
a = list(map(int, input().split()))
print(get_unique_count(a, n))
