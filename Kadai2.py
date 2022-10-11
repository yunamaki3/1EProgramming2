a = [
    [60,85,70],
    [55,75,65],
    [70,60,65],
    [80,50,77],
    [65,70,85]
]
for i in range(0,5,1):
  total = 0
  for j in range(0,3,1):
    total += a[i][j]
  print(total)
