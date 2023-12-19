a, b, c, d = map(int, input().split())

if b > c > 0 and d > a and c + d > a + b and d > 0 and a % 2 == 0:
  print("Valores aceitos")
else:
  print("Valores nao aceitos")
