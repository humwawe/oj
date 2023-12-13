a = int(input())
print(f"{a // 365} ano(s)")
a %= 365
print(f"{a // 30} mes(es)")
a %= 30
print(f"{a} dia(s)")
