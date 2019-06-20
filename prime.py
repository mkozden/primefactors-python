import time
def main(number):
	counter = 0
	primesraw = []
	i = 2
	def remainingtime(i,number):
		remaining = round(((time.process_time()*number)/i)-time.process_time(),1)
		if remaining >= 31536000:
			remaining = str(round(remaining/31536000)) + " years left		"
		elif remaining >= 86400:
			remaining = str(round(remaining/86400)) + " days left		"
		elif remaining >= 3600:
			remaining = str(round(remaining/3600)) + " hours left		"
		elif remaining >= 60:
			remaining = str(round(remaining/60)) + " minutes left		"
		else:
			remaining = str(remaining) + " seconds left		"
		return remaining


	while i <= number:
		if number%i == 0:
			number = int(number//i)
			counter = counter + 1
			primesraw.append(i)
		elif i>2:
			i += 2
		else:
			i += 1
		if i < number and i%2000001 == 0: #limiting the number of print calls to minimize speed loss
			percentage = round((i / number) * 100, 2)
			print("{}% done! {}".format(percentage,remainingtime(i,number)), end="\r")
		percentage = 100
	print("{}% done in {} seconds.								".format(percentage,time.process_time()))
	print(counter," prime factors")
	primes = list(dict.fromkeys(primesraw))
	for a in primes:
			print("{}^{}".format(a,primesraw.count(a)))

if __name__ == "__main__":
	number = int(input("enter number:"))
	main(number)