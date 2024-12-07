t = int(input())
for _ in range(t):

  n, m = map(int, input().split())
  l, r = m, 10 ** 9


  def check(mid):
    cnt = 1
    for i in range(m):
      cnt *= mid - i
      if cnt >= m * n:
        return True

    return False


  while l < r:
    mid = (l + r) // 2
    if check(mid):
      r = mid
    else:
      l = mid + 1

  print(l)
