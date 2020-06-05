def diff_of_series(n):
    sqr_of_sum = (n * (n + 1))/2
    sum_of_sqrs = (n * (n + 1) * ((2 * n) + 1))/6
    return sqr_of_sum ** 2 - sum_of_sqrs

print(diff_of_series(100))
