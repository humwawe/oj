n = int(input())
x = bin(n)[2:]
res = 0
for i in reversed(x):
  if i == '0':
    res += 1
  else:
    break

print(res)
