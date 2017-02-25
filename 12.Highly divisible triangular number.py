from math import sqrt

def main():
    count = 0
    totalNumber = 0
    tmp = 10001
    result = 0
    total = 0

    while tmp != 20001:
        total = getSum(tmp)
        result = findDivisor(total)
        if len(result) > count:
            count = len(result)
            totalNumber = total
            print (count)
            print(totalNumber)

        tmp = tmp + 1
 
    # print(count)
    # print(totalNumber)


def getSum(num):
    start = 1 + num
    end = start * num

    return end/2

def findDivisor(n):
        return set(x for tup in ([i, n//i] 
            for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

if __name__ == '__main__':
    main()
