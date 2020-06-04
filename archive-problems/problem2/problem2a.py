def sum_even_fibs(upper):
    """
      computes the sum of the 
      even fibonacci numbers
      using dynamic programming
    """
    f1, f2, f, sum = 1, 2, 0, 2
    while f <= upper:
        f = f1 + f2
        f1 = f2
        f2 = f
        sum += (f % 2 == 0)*f
    return sum

print(sum_even_fibs(4000000))
    
