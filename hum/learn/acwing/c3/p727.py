n = int(input())

cx = cy = n // 2
for i in range(n):
  for j in range(n):
    if abs(i - cx) + abs(j - cy) <= n // 2:
      print("*", end='')
    else:
      print(" ", end='')
  print()
