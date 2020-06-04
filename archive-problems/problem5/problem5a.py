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

def smallest_num_div_by_all(upr):
    primes = sieve_of_eratosthenes(upr)
    factors = primes[:]
    print("FACTORS:", factors, "\n")
    for p in primes:
        expnt = 2
        while p**expnt < upr:
            factors.append(p)
            expnt += 1
    prod = 1
    for factor in factors:
        prod *= factor
    return prod

print(smallest_num_div_by_all(20))
