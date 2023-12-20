def s(a, l, r):
  a[l:r + 1] = sorted(a[l:r + 1])


n, l, r = map(int, input().split())
a = list(map(int, input().split()))
s(a, l, r)
for i in a:
  print(i, end=" ")
