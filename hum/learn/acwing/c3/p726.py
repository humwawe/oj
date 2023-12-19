n = int(input())
for _ in range(n):
  x = int(input())
  i = 2
  while i * i <= x:
    if x % i == 0:
      print(f"{x} is not prime")
      break
    i += 1
  else:
    print(f"{x} is prime")
