def calculator(a, b, operation):
   if operation == '+':
       return a + b
   elif operation == '-':
       return a - b
   elif operation == '*':
       return a * b
   elif operation == '/':
       try:
        return a / b
       except ZeroDivisionError:
        return "error, The divisor cannot be zero. "

print("Welcome to use the calculator, \nplease enter two number")
a = float(input("a: "))
b = float(input("b: "))

operator = input("please choose operator(+,-,*,/):")


print(calculator(a,b,operator))





  