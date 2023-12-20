s, a, b = input().split(",")
x = s.find(a)
y = s.rfind(b)
if x == -1 or y == -1:
  print(-1)
  exit()

if x + len(a) <= y:
  print(y - (x + len(a)))
else:
  print(-1)
