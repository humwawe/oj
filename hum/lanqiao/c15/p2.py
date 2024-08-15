def f(x):
  return (x + 1) * x // 2


n = int(input())
s = input()
q = s.split('L')

res = 0
if s[0] == 'Q' and s[n - 1] == 'Q':
  res += f(len(q[0]) + len(q[-1]))
  for i in range(1, len(q) - 1):
    res += f(len(q[i]))
else:
  for i in range(len(q)):
    res += f(len(q[i]))
print(res)
