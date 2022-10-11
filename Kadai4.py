a = [
    ["佐藤",6],["鈴木",3],["田中",5],["加藤",7],["伊藤",1]
]
for i in range(0,5,1):
  print(a[i][0] ,end=' ')
  for j in range(10):
    print("■",end=' ')
    if j>=a[i][1]-1:
      print(" ")
      break
