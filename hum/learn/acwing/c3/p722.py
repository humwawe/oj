while True:
  a, b = sorted(map(int, input().split()))
  if a <= 0:
    break
  s = 0
  for i in range(a, b + 1):
    print(i, end=" ")
    s += i
  print(f"Sum={s}")
