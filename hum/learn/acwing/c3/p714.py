a = int(input())
b = int(input())
a, b = min(a, b), max(a, b)
s = 0
for i in range(a + 1, b):
  if i % 2 == 1:
    s += i
print(s)
