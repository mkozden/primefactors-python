import math


def main(number):
    num2 = number
    print("{}! is {}".format(num2, math.factorial(num2)))
    primes = []
    used = []
    i = 2
    while i < number:
        if i not in used:
            x = i
            count = 0
            n = 1
            while x <= number:
                if x % i == 0:
                    count += int(math.floor(number/x))
                    a = 1
                    while a*x <= number:
                        used.append(a*x)
                        a += 1
                    n += 1
                    x = i**n
                else:
                    x = i**n
            primes.append([i, count])
            i += 1
        else:
            i += 1
    print("The factors of {}! are:".format(num2))
    for [x, y] in primes:
        print("{}^{}".format(x, y))


if __name__ == "__main__":
    getnumber = int(input("enter number:"))
    main(getnumber)
