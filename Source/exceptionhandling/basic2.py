num1 = int(input("Enter the number1"))
num2 = int(input("Enter the number2"))

try:
    num3 = num1 / num2
    print(f'{num1} divided by {num2} is {num3}')
except Exception:
    print(f'{num1} divided by {num2} is infinity ')
finally:
    print("I will be executed always")




