from itertools import pairwise

s = input()
for x, y in pairwise(s):
  if x > y:
    print("No")
    break
else:
  print("Yes")
