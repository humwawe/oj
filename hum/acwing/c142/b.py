from collections import Counter

n = int(input())
a, b, c = input(), input(), input()
l = len(a)
cnt_a, cnt_b, cnt_c = Counter(a), Counter(b), Counter(c)


def f(cnt):
  res = 0
  for k, v in cnt.items():
    left = l - v
    if left == 0 and n == 1:
      res = max(res, l - 1)
    else:
      res = max(res, v + min(n, left))
  return res


res1, res2, res3 = f(cnt_a), f(cnt_b), f(cnt_c)
m = max(res1, res2, res3)
m_cnt = 0
res = ''
if m == res1:
  m_cnt += 1
  res = "A"
if m == res2:
  m_cnt += 1
  res = "B"
if m == res3:
  m_cnt += 1
  res = "C"
if m_cnt > 1:
  print("D")
else:
  print(res)
