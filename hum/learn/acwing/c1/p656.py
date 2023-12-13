a = float(input())
a = int(a * 100)

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % (a // 10000))
a %= 10000
print("%d nota(s) de R$ 50.00" % (a // 5000))
a %= 5000
print("%d nota(s) de R$ 20.00" % (a // 2000))
a %= 2000
print("%d nota(s) de R$ 10.00" % (a // 1000))
a %= 1000
print("%d nota(s) de R$ 5.00" % (a // 500))
a %= 500
print("%d nota(s) de R$ 2.00" % (a // 200))
a %= 200

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % (a // 100))
a %= 100
print("%d moeda(s) de R$ 0.50" % (a // 50))
a %= 50
print("%d moeda(s) de R$ 0.25" % (a // 25))
a %= 25
print("%d moeda(s) de R$ 0.10" % (a // 10))
a %= 10
print("%d moeda(s) de R$ 0.05" % (a // 5))
a %= 5
print("%d moeda(s) de R$ 0.01" % a)
