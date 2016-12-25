

def main():
    limit = 100
    sumOfSquare = limit*(1+limit)/2
    sumOfSquare = sumOfSquare * sumOfSquare
    result = sumOfSquare - (2*limit +1) * limit*(1+limit)/6
    print result


if __name__ == '__main__':
    main()