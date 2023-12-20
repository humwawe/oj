from collections import Counter

_ = input()
a = list(Counter(map(int, input().split())).items())

a.sort(key=lambda i: (-i[1], i[0]))
print(a[0][0])
