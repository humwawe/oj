a = [0] * 20
for i in range(20):
  a[i] = int(input())

a.reverse()
for i in range(20):
  print(f"N[{i}] = {a[i]}")
