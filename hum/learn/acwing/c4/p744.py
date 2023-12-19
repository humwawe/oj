c = int(input())
t = input()
m = []
n = 12
for i in range(n):
  tmp = list(map(float, input().split()))
  m.append(tmp)

s = 0
for i in range(n):
  s += m[i][c]
if t == "S":
  print(f"{s:.1f}")
else:
  print(f"{s / 12:.1f}")
