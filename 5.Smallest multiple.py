# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

def main():
    result = 2520

    for x in xrange(1,100000000):
        result = result + 10
        if test(result):
            break



def test(number):
    if number % 19 != 0 or number % 18 != 0 or number % 17 != 0 or number % 16 != 0 or number % 13 != 0:
        return False
    if number % 11 != 0 or number % 12 != 0 or number % 14 != 0:
        return False
    
    print number
    return True

if __name__ == '__main__':
    main()