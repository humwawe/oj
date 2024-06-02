class Solution:
  def clearStars(self, s: str) -> str:
    n = len(s)
    vis = [0] * n
    idx = [[] for _ in range(26)]
    for i in range(n):
      if s[i] == '*':
        for j in range(26):
          if idx[j]:
            vis[idx[j].pop()] = 1
            break
      else:
        idx[ord(s[i]) - ord('a')].append(i)
    res = []
    for i in range(n):
      if not vis[i] and s[i] != '*':
        res.append(s[i])

    return ''.join(res)
