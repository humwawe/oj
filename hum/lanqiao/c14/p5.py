mod = 998244353

a = list(map(int, input().split()))

length = sum(a)

pow10 = [1]
ann = [1]

for i in range(1, length + 1):
  pow10.append(pow10[-1] * 10 % mod)
  ann.append(ann[-1] * i % mod)

t = 1
for i in range(9):
  t = t * ann[a[i]] % mod

t = pow(t, -1, mod)
t = t * ann[length - 1] % mod

acc = 0
for i in range(9):
  acc = (acc + (i + 1) * t * a[i]) % mod

res = 0
for i in range(length):
  res = (res + pow10[i] * acc) % mod

print(res)
