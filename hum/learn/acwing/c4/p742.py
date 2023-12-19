n = int(input())
a = list(map(int, input().split()))
print(f"Minimum value: {min(a)}")
print(f"Position: {a.index(min(a))}")
