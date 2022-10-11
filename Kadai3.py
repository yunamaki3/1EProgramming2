a = input().split(',')
min = int(a[0])
for i in range(1,len(a),1):
  if min > int(a[i]):
    min = int(a[i])
print("最小値は",min)
