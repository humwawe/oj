a = [0.0] * 100
for i in range(100):
  a[i] = float(input())
  if a[i] <= 10:
    print(f"A[{i}] = {a[i]}")
