k = float(input())
a = input()
b = input()
cnt = 0
for x, y in zip(a, b):
  if x == y:
    cnt += 1
if cnt / len(a) >= k:
  print("yes")
else:
  print("no")
