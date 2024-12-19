# Create a list containing all prime numbers from 1 to 50.
# output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

primes = [n for n in range(2, 51) if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]
print(primes)
