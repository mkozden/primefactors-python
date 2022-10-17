import time
import os
from tqdm import tqdm


def main(number):
	counter = 0
	primesraw = []
	i = 2
	sqrtnum = number ** 0.5
	pbar = tqdm(total=sqrtnum)
	while i <= sqrtnum:
		if number % i == 0:
			number = int(number // i)
			sqrtnum = number ** 0.5
			pbar.reset(total=sqrtnum)
			pbar.update(i)
			counter += 1
			primesraw.append(i)
		elif i > 2:
			i += 2
			pbar.update(2)
		else:
			i += 1
			pbar.update(1)
	pbar.close()
	primesraw.append(number)
	counter += 1
	os.system("cls||clear")
	print(f"100% done in {time.process_time()} seconds.")
	print(counter, " prime factors")
	primes = list(dict.fromkeys(primesraw))
	for a in primes:
		print("{}^{}".format(a, primesraw.count(a)))


if __name__ == "__main__":
	getnumber = input("enter number or expression (must result in integer value):")
	if any(opr in getnumber for opr in ["-", "+", "*", "/", "%"]):
		try:
			getnumber = eval(getnumber)
			if isinstance(getnumber, int):
				main(getnumber)
			else:
				raise TypeError("Not an integer!")
		except SyntaxError:
			print("Invalid expression")
	else:
		try:
			main(int(getnumber))
		except ValueError:
			print("Not an integer!")
