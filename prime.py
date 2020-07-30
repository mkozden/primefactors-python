import time
import math


def main(number):
	counter = 0
	primesraw = []
	i = 2
	def elapsedtime():
		elapsed = round(time.process_time(),2)
		if elapsed >= 31536000:
			elapsed = str(round(elapsed/31536000)) + " years 		"
		elif elapsed >= 86400:
			elapsed = str(round(elapsed/86400)) + " days 		"
		elif elapsed >= 3600:
			elapsed = str(math.floor(elapsed/3600))+" hours "+str(round(math.floor((elapsed - math.floor(elapsed/3600)*3600)/60)))+" minutes"
		elif elapsed >= 60:
			elapsed = str(math.floor(elapsed/60))+" minutes "+str(round(elapsed - math.floor(elapsed/60)*60))+" seconds"
		else:
			elapsed = str(elapsed) + " seconds 		"
		return elapsed
		

	while i <= number**0.5:
		if number % i == 0:
			number = int(number//i)
			counter += 1
			primesraw.append(i)
		elif i > 2:
			i += 2
		else:
			i += 1
		percentage = round(i*100/number,2)
		if i % 50001 == 0:
			print("{}                           ".format (elapsedtime()), end="\r")
	primesraw.append(number)
	counter += 1
	percentage = 100
	print("{}% done in {} 								.".format(percentage, elapsedtime()))
	print(counter, " prime factors")
	primes = list(dict.fromkeys(primesraw))
	for a in primes:
			print("{}^{}".format(a, primesraw.count(a)))


if __name__ == "__main__":
	getnumber = int(input("enter number:"))
	main(getnumber)
