import math

a, b, c = map(float, input().split())
if b * b - 4 * a * c < 0 or a == 0:
  print("Impossivel calcular")
else:
  print(f"R1 = {(-b + math.sqrt(b * b - 4 * a * c)) / 2 / a:.5f}")
  print(f"R2 = {(-b - math.sqrt(b * b - 4 * a * c)) / 2 / a:.5f}")
