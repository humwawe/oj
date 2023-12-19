a, b, c, d = map(float, input().split())
x = (a * 2 + b * 3 + c * 4 + d) / 10
print("Media: %.1f" % x)

if x >= 7:
  print("Aluno aprovado.")
elif x < 5:
  print("Aluno reprovado.")
else:
  print("Aluno em exame.")
  y = float(input())
  print("Nota do exame: %.1f" % y)
  z = (x + y) / 2
  if z >= 5:
    print("Aluno aprovado.")
  else:
    print("Aluno reprovado.")
  print("Media final: %.1f" % z)
