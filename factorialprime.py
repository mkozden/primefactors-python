factinput = int(input("Enter a number:"))
counter = 0
print("The primes of ",factinput,"! are:")
primes = []
for num in range(2,factinput + 1):
   # prime numbers are greater than 1
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
    print(i,"^",factorialprimes(factinput,i))

