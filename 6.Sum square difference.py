

def main():
    sumOfSquare = 100*(1+100)/2
    sumOfSquare = sumOfSquare * sumOfSquare
    result = 0

    for x in xrange(1,101):
        result += x * x

    print sumOfSquare - result


if __name__ == '__main__':
    main()