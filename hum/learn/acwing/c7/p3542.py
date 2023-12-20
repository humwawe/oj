_ = input()
a = set(map(int, input().split()))
_ = input()
b = list(map(int, input().split()))
for i in b:
  if i in a:
    print("YES")
  else:
    print("NO")
