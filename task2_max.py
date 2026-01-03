def  max_of_two(num1, num2):
    return  num1>num2

num1=int(input("Введіть перше число"))
num2=int(input("Введіть друге число"))
if max_of_two(num1,num2):
    print(f'Число {'num1'} більше за {'num2'}')
else:
    print(f'Число {'num1'} менше за {'num2'}')
