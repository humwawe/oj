t = input()
m = []
n = 12
for i in range(n):
  tmp = list(map(float, input().split()))
  m.append(tmp)

s = 0
cnt = 0
for i in range(n):
  for j in range(n):
    if i + j < 11 and i > j:
      s += m[i][j]
      cnt += 1

if t == "S":
  print(f"{s:.1f}")
else:
  print(f"{s / cnt:.1f}")
