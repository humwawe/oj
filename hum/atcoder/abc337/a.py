n = int(input())
s1, s2 = 0, 0
for _ in range(n):
  x, y = map(int, input().split())
  s1 += x
  s2 += y
if s1 > s2:
  print("Takahashi")
elif s1 < s2:
  print("Aoki")
else:
  print("Draw")
