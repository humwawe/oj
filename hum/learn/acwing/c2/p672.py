a = float(input())
if a <= 2000:
  print("Isento")
else:
  res = 0
  if a > 2000:
    res += (min(3000.0, a) - 2000) * 0.08
  if a > 3000:
    res += (min(4500.0, a) - 3000) * 0.18
  if a > 4500:
    res += (min(5000.0, a) - 4500) * 0.28

  print(f"R$ {res:.2f}")
