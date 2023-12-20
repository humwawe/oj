s = input()
res = []
for c in s:
  if 'a' <= c <= 'z':
    res.append(chr(ord('a') + (ord(c) - ord('a') + 1) % 26))
  elif 'A' <= c <= 'Z':
    res.append(chr(ord('A') + (ord(c) - ord('A') + 1) % 26))
  else:
    res.append(c)
print("".join(res))
