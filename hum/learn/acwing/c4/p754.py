while True:
  n = int(input())
  if n == 0:
    break
  a = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    for j in range(n):
      a[i][j] = abs(i - j)
      print(a[i][j] + 1, end=" ")
    print()
  print()
