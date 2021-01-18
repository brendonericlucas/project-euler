# find the sum of all of the distinct primes less than 2 million

# let isPrime(n) = True if n is prime and = False otherwise
# if isPrime(n) is efficient, then we can loop over all values n
# in [1, 2,000,000) and accumulate those for which isPrime(n) = True
# what will matter here is how dense the primes are in [1, 2,000,000)
# for example, suppose - contrary to fact - that there is only one prime
# in the half-open 'interval' [1, 2,000,000). Then an efficient test of the
# primality of some n in [1, 2,000,000) would be to simply compare n to the
# sole prime p.

# by defintion, a positive integer n is prime if
# 1) n > 1
# 2) the only positive integer divisors of n are 1 and n itself
import math

primes = [2] # initialize list of primes to 2
def generate_primes(lower=2, upper=2000000):
    for integer in range(lower + 1, upper, 2): # we can ignore all even n > 2
        isPrime = True # assume integer is prime
        for prime in primes: # divide integer by each prime in asc order
            if prime > math.sqrt(integer): # all distinct factors of integer are < sqrt(n)
                break
            if integer % prime == 0: # check if integer is evenly divisible by prime
                isPrime = False # isPrime = False if prime divides integer
                break # we now know that integer is not prime, so exit the for loop
        if isPrime: # since integer is prime, we add it to primes
            primes.append(integer)
    return sum(primes)

print(generate_primes())
