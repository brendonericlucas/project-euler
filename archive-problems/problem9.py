# given constraints
# a, b, c are natural numbers
# a < b < c
# a + b + c = 1000

# required: a^2 + b^2 = c^2

# observations
# a and b values determine c values c = 1000 - (a + b)
# this is a plane in 3 - space, I believe
# a = 1, b = 2, c = 997 <-- least values for a, and b'
# a = 332, b = 333,  c = 335 <-- greatest value for a
# a = 1, b = 499, c = 500 <-- greatest value for b

# for a in 1...332: <-- loop through the possible values of a
#   b = a + 1 <-- b must be at least one more than a
#   c = 1000 - (a + b) <-- c is determined as the difference between 1000 and (a + b)
#   while b < c: <-- ignore combinations that don't satisfy our constraints
#     if a^2 + b^2 = c^2: <-- check if is pythagorean triple
#       return (a, b, c)  <-- return pythagorean triple
#     else:
#       b += 1 <-- no triple found, so increment b by one and keep looping / searching

found = False
for a in range(1, 333):
    if not found:
        print(a)
        b = a + 1
        c = 1000 - (a + b)
        while b < c:
            if a**2 + b**2 == c**2:
                print(a, b, c)
                print(a*b*c)
                found = True
                break
            else:
                b += 1
                c = 1000 - (a + b)
    else:
        break
