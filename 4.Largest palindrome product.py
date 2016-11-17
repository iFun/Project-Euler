

def solution():
    result = 0
    num1 = 999
    num2 = 999

    while num1 > 0 and num2 > 0:
        if isPalindrome(num1 * num2):
            result = num2 * num1
            print num1
            print num2
            break
        if num1 == num2:
            num1 -= 1
        else:
            num2 -= 1


    print result

def isPalindrome(num):
    number = num
    rev = 0
    while number > 0:
        lastDigit = number % 10
        rev = rev * 10 + lastDigit
        number = number / 10

    return num == rev

solution()