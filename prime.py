def main():
	number = int(input("enter number:"))
	num2 = number
	counter = 0
	primesraw = []
	i = 2
	while i <= number:
		if number%i == 0:
			number = number/i
			counter = counter + 1
			primesraw.append(i)
		else:
			i += 1
	print(counter," prime factors")
	primes = list(dict.fromkeys(primesraw))
	for a in primes:
			print("{}^{}".format(a,primesraw.count(a)))

if __name__ == "__main__":
	main()