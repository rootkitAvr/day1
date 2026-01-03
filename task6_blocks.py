def input_number():
    return int(input())
def check_even(n):
    return n % 2 ==0
def main():
    num = input_number()
    if check_even(num):
        print('Парне')
    else:
        print('Непарне')

main()