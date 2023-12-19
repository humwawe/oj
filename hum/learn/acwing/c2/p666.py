c, b, a = sorted(map(float, input().split()))

if a >= b + c:
  print("NAO FORMA TRIANGULO")
else:
  if a * a == b * b + c * c:
    print("TRIANGULO RETANGULO")
  if a * a > b * b + c * c:
    print("TRIANGULO OBTUSANGULO")
  if a * a < b * b + c * c:
    print("TRIANGULO ACUTANGULO")
  if a == b == c:
    print("TRIANGULO EQUILATERO")
  elif a == b or b == c:
    print("TRIANGULO ISOSCELES")
