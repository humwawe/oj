def copy(a, b, size):
  for i in range(size):
    b[i] = a[i]


n, m, size = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
copy(a, b, size)
for i in b:
  print(i, end=" ")
