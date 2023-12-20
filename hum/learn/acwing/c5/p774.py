s = input()
s = s[:-1]
res = ""
for i in s.split():
  if len(i) > len(res):
    res = i
print(res)
