import math
import time
def main():

    def remainingtime(i, number):
        remaining = round(((time.process_time() * number) / i) - time.process_time(), 1)
        if remaining >= 86400:
            remaining = str(round(remaining / 86400)) + " days left		"
        elif remaining >= 3600:
            remaining = str(round(remaining / 3600)) + " hours left		"
        elif remaining >= 60:
            remaining = str(round(remaining / 60)) + " minutes left		"
        else:
            remaining = str(remaining) + " seconds left		"
        return remaining
    number = int(input("Enter a number:"))
    num2 = number
    print("{}! is {}".format(num2,math.factorial(num2)))
    primes = []
    used = []
    i = 2
    while i < number:
        if i not in used:
            x = i
            count = 0
            n = 1
            while x < number:
                if x%i == 0:
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
    for [x,y] in primes:
        print("{}^{}".format(x,y))

if __name__ == "__main__":
    main()
