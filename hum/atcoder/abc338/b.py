from collections import Counter

s = input()
cnt = Counter(s)
max_v = max(cnt.values())
for key in sorted(cnt.keys()):
  if cnt[key] == max_v:
    print(key)
    break
