n = int(input())
cnt = 0

while n < 1000 and cnt < 6:
  if n % 2 == 1:
    cnt += 1
    print(n)
  n += 1
