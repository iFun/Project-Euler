# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

def main():
    a = 0
    b = 1
    c = 0

    while a < 350:
        b = a + 1  
        while b < 1000 - b - a:
            c = 1000 - a - b
            if a * a + b * b == c * c:
                print 'a: ' + str(a) + 'b: ' + str(b) + 'c: ' + str(c)
                print a*b*c
            b += 1

        a += 1
        

    print 'done'

if __name__ == '__main__':
    main()