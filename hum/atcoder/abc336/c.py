n = int(input()) - 1
res = ""
while n > 0:
  n, x = divmod(n, 5)
  res = str(x * 2) + res

print(max(res, "0"))
