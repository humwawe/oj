n = int(input())
for _ in range(n):
  a, b = input().split()
  x, y = 0, 0
  if a == "Bear":
    x = 1
  elif a == "Gun":
    x = 2
  if b == "Bear":
    y = 1
  elif b == "Gun":
    y = 2

  if x == y:
    print("Tie")
  elif x == (y + 1) % 3:
    print("Player1")
  else:
    print("Player2")
