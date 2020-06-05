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

def bound_nth_prime(n):
    return math.ceil( n * ( math.log(n) + math.log(math.log(n)) ) )

print((sieve_of_eratosthenes(bound_nth_prime(10001))[10000]))
