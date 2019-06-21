import time
import math


def main(number):
	counter = 0
	primesraw = []
	i = 2

	def remainingtime(divisor, dividend):
		remaining = round(((time.process_time()*dividend)/divisor)-time.process_time(), 2)
		if remaining >= 31536000:
			remaining = str(round(remaining/31536000)) + " years 		"
		elif remaining >= 86400:
			remaining = str(round(remaining/86400)) + " days 		"
		elif remaining >= 3600:
			remaining = str(math.floor(remaining/3600))+" hours "+str(round((remaining - math.floor(remaining))*60))+" minutes"
		elif remaining >= 60:
			remaining = str(math.floor(remaining/60))+" minutes "+str(round((remaining - math.floor(remaining))*60))+" seconds"
		else:
			remaining = str(remaining) + " seconds 		"
		return remaining

	while i <= number:
		if number % i == 0:
			number = int(number//i)
			counter = counter + 1
			primesraw.append(i)
		elif i > 2:
			i += 2
		else:
			i += 1
		if i < number and i % 2000001 == 0:  # limiting the number of print calls to minimize speed loss
			percentage = round((i / number) * 100, 2)
			print("{}% done! {} left				".format(percentage, remainingtime(i, number)), end="\r")
	percentage = 100
	print("{}% done in {} 								.".format(percentage, remainingtime(i, number)))
	print(counter, " prime factors")
	primes = list(dict.fromkeys(primesraw))
	for a in primes:
			print("{}^{}".format(a, primesraw.count(a)))


if __name__ == "__main__":
	getnumber = int(input("enter number:"))
	main(getnumber)
