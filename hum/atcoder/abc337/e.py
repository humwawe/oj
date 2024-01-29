n = int(input())
m = (n - 1).bit_length()
print(m)
for i in range(m):
  tmp = []
  for j in range(n):
    if j >> (m - i - 1) & 1 == 1:
      tmp.append(j + 1)
  print(len(tmp), *tmp, sep=' ')
s = input()

print(int(s, 2) + 1)
