s = input()
a = input()
b = input()
res = []
for sub in s.split():
  if sub == a:
    res.append(b)
  else:
    res.append(sub)

print(" ".join(res))
