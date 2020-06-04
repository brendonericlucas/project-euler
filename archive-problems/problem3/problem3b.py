import math
from itertools import compress

def sieve_of_eratosthenes(n):
    """
      implements the sieve_of
      eratosthenes; compare 
      the time complexity of
      this function to the 
      function using trial 
      division in sol 3a
    """
    is_prime = [True]*(n + 1)
    is_prime[0] = False
    is_prime[1] = False
    bound = int(math.floor(math.sqrt(n)))
    for i in range(2, bound + 1):
        if is_prime[i] == True:
            for j in range(i**2, n + 1, i):
                is_prime[j] = False

    return list(compress(range(len(is_prime)), is_prime))

#print(sieve_of_eratosthenes(775146))

def largest_prime_factor(num):
    """ returns the largest prime factor of num """
    n = math.floor(math.sqrt(num))
    primes = reversed(sieve_of_eratosthenes(n))
    for p in primes:
        if num % p == 0:
            return p

print(largest_prime_factor(600851475143))
    
