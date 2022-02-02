import time


def is_palindrome(val):
    return str(val) == str(val)[::-1]


def palindrome():
    start_time = time.time()
    palindrome_list = []
    low_val = 900
    high_val = 999
    for num1 in range(low_val, high_val):
        for num2 in range(low_val, high_val):
            if is_palindrome(num1*num2):
                palindrome_list.append(num1*num2)
    print(f'Palindrome list {palindrome_list}')
    print(f'Highest palindrome: {max(palindrome_list)}')
    print(f'Runtime:', time.time()-start_time)


palindrome()
