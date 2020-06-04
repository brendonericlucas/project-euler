def multiple_of(num, div):
    """ 
       returns true iff
       num is a multiple
       of div 
    """
    return num % div == 0

def sum_multiples(upper):
    """
       computes the sum of 
       all multiples of 3 or 5
       in [1, upper)
    """
    sum = 0
    for i in range(1, upper):
        sum += (multiple_of(i, 3) or multiple_of(i, 5))*i
    return sum

print(sum_multiples(1000))
