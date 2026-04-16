def calculator(a, b, operation):
   if operation == 'add':
       return a + b
   elif operation == 'subtract':
       return a - b
   elif operation == 'multiply':
       return a * b
   elif operation == 'divide':
       return a / b
print(calculator(10, 5, 'add')) # 15
print(calculator(10, 5, 'subtract')) # 5
print(calculator(10, 5, 'multiply')) # 50
print(calculator(10, 5, 'divide')) # 2.0