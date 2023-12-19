res = (0, 0)
for i in range(100):
  x = int(input())
  if x > res[0]:
    res = (x, i)

print(res[0])
print(res[1] + 1)
