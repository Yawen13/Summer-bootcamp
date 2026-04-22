print("请输入任意数字,用于求平均数(输入q停止)")
total=0
count=0
number=input()
while number!="q":
    num=float(number)
    total+=num
    count+=1
    number=input()

if count==0:
  print("必须输入数字才可以计算！")
else:
  average=total/count
  print("你输入的数字平均值:", average)