import math

def has_divisor(num, arr):
    """ tests if num has a
        divisor in arr
    """
    for divisor in arr:
        if num % divisor == 0:
            return True
    return False

def primes(upper):
    """
       uses to trial divison
       to generate all primes
       in range [2, upper]
    """
    primes = [2]
    for n in range(3, upper+1, 2):
        if not has_divisor(n, primes):
            primes.append(n)
    return primes
        

def largest_prime_factor(num):
    """
       computes largest prime
       factor of num
    """
    upper = int(math.floor(math.sqrt(num)))
    prime = reversed(primes(upper))
    for p in prime:
        if num % p == 0:
            return p

print(largest_prime_factor(600851475143))
    
 
