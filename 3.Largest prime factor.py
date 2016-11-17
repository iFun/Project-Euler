# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math

def solution():
    num = 600851475143/6857
    result = 0
    maximum = 0


    for x in xrange(5,num/6857):
        if num % x == 0:
            print x
            num = num / x
            if x > result:
                result = x
        x += 2

    print result

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


if is_prime(6857):
    print'good'