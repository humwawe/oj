a, m, l, r = map(int, input().split())

x = (l - a + m - 1) // m
y = (r - a) // m
print(y - x + 1)
