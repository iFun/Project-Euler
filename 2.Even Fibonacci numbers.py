# By considering the terms in the Fibonacci sequence 
#whose values do not exceed four million, find the sum of the even-valued terms.
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89,

def solution():
    
    prev = 1
    curr = 2
    next_val = 0
    result = 2
    
    while next_val <= 4000000:
        next_val = prev + curr
        if next_val % 2 == 0:

            result += next_val

        prev = curr
        curr = next_val

    print result  

solution()