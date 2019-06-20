import prime, factorialprime

print("Press 1 for finding primes of an integer")
print("Press 2 for finding primes of a factorial")
choice = int(input("Your choice:"))

if choice == 1:
	number = int(input("enter number:"))
	prime.main(number)
elif choice == 2:
    factorialprime.main()

