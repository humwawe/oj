a, b, c, d = map(int, input().split())
t = c * 60 + d - a * 60 - b
if t <= 0:
  t += 60 * 24
print(f"O JOGO DUROU {t // 60} HORA(S) E {t % 60} MINUTO(S)")
