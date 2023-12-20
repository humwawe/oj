a, b = input().split()
a, b = (b, a) if len(a) > len(b) else (a, b)
if a in b + b:
  print("true")
else:
  print("false")
