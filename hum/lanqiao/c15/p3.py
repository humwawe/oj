n = int(input())
a = map(int, input().split())
l1, l2 = [], []

for c in a:
  if c > 0:
    l1.append(c)
  elif c < 0:
    l2.append(c)
l1.append(0)
l2.append(0)

s1, s2 = sum(l1), -sum(l2)
m1, m2 = max(l1), -min(l2)

if (s1 >= s2 - m2 and s1 <= s2) or (s2 >= s1 - m1 and s2 <= s1):
  print("Y")
else:
  print("N")
