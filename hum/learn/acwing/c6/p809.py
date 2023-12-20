import math


def lcm(a, b):
  return a * b * math.gcd(a, b)


a, b = map(int, input().split())
print(lcm(a, b))
