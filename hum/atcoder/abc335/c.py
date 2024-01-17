n, q = map(int, input().split())
sum_p = [(1, 0)]

for _ in range(q):
  t, x = input().split()
  if t == '1':
    if x == 'R':
      sum_p.append((sum_p[-1][0] + 1, sum_p[-1][1]))
    elif x == 'L':
      sum_p.append((sum_p[-1][0] - 1, sum_p[-1][1]))
    elif x == 'U':
      sum_p.append((sum_p[-1][0], sum_p[-1][1] + 1))
    else:
      sum_p.append((sum_p[-1][0], sum_p[-1][1] - 1))
  else:
    x = int(x)
    l = len(sum_p) - 1
    if x > l:
      print(x - l, 0)
    else:
      print(sum_p[l - x + 1][0], sum_p[l - x + 1][1])
