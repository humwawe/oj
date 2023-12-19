a, b = 0, 1
res = [a, b]
for i in range(2, 65):
  res.append(res[i - 1] + res[i - 2])
n = int(input())

for _ in range(n):
  i = int(input())
  print(f"Fib({i}) = {res[i]}")
