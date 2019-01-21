import math
factinput = int(input("Enter a number:"))
print("The primes of {}! are:".format(factinput))
primes = []
for num in range(2,factinput + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           primes.append(num)
def factorialprimes(factinput,x):
    divided = []
    while factinput > x:
        divided.append(int(factinput/x))
        factinput = factinput/x
    return sum(divided)



for i in primes:
    print("{}^{}".format(i,factorialprimes(factinput,i)))

print("So {}! is equal to: {}".format(factinput,math.factorial(factinput)))

