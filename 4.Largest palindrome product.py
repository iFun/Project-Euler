
def solution():
    result = 0
    num1 = 999
    num2 = 999

    while num1 > 1 and num2 > 500:
        if isPalindrome(num1 * num2):
            if num2 * num1 > result:
                result = num2 * num1
            num2 -= 1
            num1 = 999
        num1 -= 1

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