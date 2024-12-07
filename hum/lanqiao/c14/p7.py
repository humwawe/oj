t = int(input())
for _ in range(t):

  n, m = map(int, input().split())
  s1 = input()
  s2 = input()
  flg = False
  if s1 == s2 or s1 == s2[::-1]:
    flg = True

  elif n > 1:
    s1 = s1[:-1]
    if s1 == s2:
      flg = True
    elif len(set(s1) | set(s2)) == 1 and n > m:
      flg = True
    elif s1 == s1[::-1] and s1[:-1] == s2:
      flg = True

  print('red' if flg else 'blue')
