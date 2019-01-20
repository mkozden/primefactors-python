number = int(input("enter number:"))
num2 = number
counter = 0
primes = []
numfinal = 0
for i in range(2,number+1):
	while number%i == 0:
		number = number/i
		counter = counter + 1
		primes.append(i)
print(counter," prime factors")
while True:
	for a in range(2,num2+1):
		if a in primes:
			print("{}^{}".format(a,primes.count(a)))
			numfinal += (a**primes.count(a))
		if num2 == numfinal:
			break
	break