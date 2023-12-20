while True:
  x = int(input())
  if x == 0:
    exit()
  tmp = []
  for _ in range(x):
    tmp.append(input())
  cur = tmp[0]
  for i in range(len(cur)):
    w = cur[i:len(cur)]
    for j in range(1, x):
      if not tmp[j].endswith(w):
        break
    else:
      print(w)
      break
  else:
    print()
