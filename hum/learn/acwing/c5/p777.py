while True:
  s = input()
  if s == ".":
    break
  n = len(s)
  for i in range(1, n + 1):
    if n % i == 0 and s[0:i] * (n // i) == s:
      print(n // i)
      break
