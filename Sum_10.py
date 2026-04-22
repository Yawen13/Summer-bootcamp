#循环输入数字，直到输入 0 停止，求总和
s = 0
i=1
while i!=0:
  i=float(input("please enter a number"))
  s+=i

print("sum:",s)