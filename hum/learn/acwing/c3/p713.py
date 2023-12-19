n = int(input())
cnt = 0
for i in range(n):
  x = int(input())
  if 10 <= x <= 20:
    cnt += 1
print(cnt, end=" in\n")
print(n - cnt, end=" out\n")
